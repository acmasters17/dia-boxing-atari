import os
from stable_baselines3.common.callbacks import BaseCallback


class SaveOnBestTrainingRewardCallback(BaseCallback):
    def __init__(self, check_freq: int, save_path: str, verbrose=1):
        super(SaveOnBestTrainingRewardCallback,self).__init__(verbrose)
        self.check_freq = check_freq
        self.save_path = save_path

    def _init_callback(self) -> None:
        # Create filder for saved models
        if (self.save_path is not None):
            os.makedirs(self.save_path,exist_ok=True)


    def _on_step(self) -> bool:
        if(self.n_calls % self.check_freq == 0):
            model_path = os.path.join(self.save_path, 'best_model_{}'.format(self.n_calls))
            self.model.save(model_path)

        return True
