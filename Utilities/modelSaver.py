import os
import numpy as np
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.results_plotter import load_results, ts2xy
from stable_baselines3.common.callbacks import BaseCallback


class SaveOnBestTrainingRewardCallback(BaseCallback):
    def __init__(self, check_freq: int, save_path: str, algorithm_name: str, verbose: int = 1):
        super(SaveOnBestTrainingRewardCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.save_path = save_path
        self.log_dir = os.path.join(save_path, 'local_logs')
        self.model_save_path = os.path.join(save_path, 'models', algorithm_name)
        self.best_model_save_path = os.path.join(self.model_save_path, 'best_model')
        self.best_mean_reward = -np.inf

    def _init_callback(self) -> None:
        # Create folder if needed
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self) -> bool:
        # if we have reached timestamp threshold
        if self.n_calls % self.check_freq == 0:
          # Retrieve training reward from local logs
          x, y = ts2xy(load_results(self.log_dir), 'timesteps')
          if len(x) > 0:
              # get the mean training reward over the last 100 episodes
              mean_reward = np.mean(y[-100:])
              if self.verbose > 0:
                # Print it out
                print(f"Num timesteps: {self.num_timesteps}")
                print(f"Best mean reward: {self.best_mean_reward:.2f} - Last mean reward per episode: {mean_reward:.2f}")

              # save this model
              self.model.save(os.path.join(self.model_save_path, 'model_at_{}'.format(self.num_timesteps)))
              

              # if we get a new best model, then save here
              if mean_reward > self.best_mean_reward:
                  self.best_mean_reward = mean_reward
                  if self.verbose > 0:
                    print(f"Saving new best model to {self.best_model_save_path}")
                  self.model.save(self.best_model_save_path)

        return True
