import os
from matplotlib import pyplot as plt
from Utilities.modelSaver import SaveOnBestTrainingRewardCallback
from stable_baselines3.common import results_plotter
from stable_baselines3 import A2C, DQN, PPO
from stable_baselines3.common.results_plotter import plot_results
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack




# So this is going to the model training main that is used to train RL algorithms
# When run it will train a reinforcement learning model based of input parameters
CHECKPOINT_DIR = './TrainingInfo/'
LOCAL_LOGS_DIR = './TrainingInfo/local_logs'
TENSORBOARD_LOGS_DIR = './TrainingInfo/tensorboard_logs/'
TIMESTAMPS = 1000000
os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
callback = SaveOnBestTrainingRewardCallback(check_freq=2500,save_path=CHECKPOINT_DIR, algorithm_name="PPO_CnnPolicy")
env = make_atari_env('BoxingNoFrameskip-v4', n_envs=4, seed=0, monitor_dir=LOCAL_LOGS_DIR)
env = VecFrameStack(env,n_stack=4)
model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=TENSORBOARD_LOGS_DIR)
model.learn(total_timesteps=TIMESTAMPS, callback=callback)

plot_results([LOCAL_LOGS_DIR], TIMESTAMPS, results_plotter.X_TIMESTEPS, "PPO_CnnPolicy Boxing Over 1 million training cycles")
plt.show()
exit(0)

