import os
import random
import gym
from matplotlib import pyplot as plt
import numpy as np
from Utilities.modelSaver import SaveOnBestTrainingRewardCallback
from stable_baselines3.common import results_plotter
from stable_baselines3 import A2C, DQN, TD3
from stable_baselines3.common.results_plotter import plot_results
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack




# So this is going to the model training main that is used to train RL algorithms
# When run it will train a reinforcement learning model based of input parameters
CHECKPOINT_DIR = './TrainingInfo/'
LOCAL_LOGS_DIR = './TrainingInfo/local_logs'
TENSORBOARD_LOGS_DIR = './TrainingInfo/tensorboard_logs/'
TIMESTAMPS = 5000000
os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
callback = SaveOnBestTrainingRewardCallback(check_freq=2500,save_path=CHECKPOINT_DIR, algorithm_name="DQN_CnnPolicy")
env = make_atari_env('BoxingNoFrameskip-v4', n_envs=2, seed=0, monitor_dir=LOCAL_LOGS_DIR)
# Frame-stacking with 4 frames
env = VecFrameStack(env, n_stack=2)
model = DQN('CnnPolicy', env, verbose=1, tensorboard_log=TENSORBOARD_LOGS_DIR)
model.learn(total_timesteps=TIMESTAMPS, callback=callback)

plot_results([LOCAL_LOGS_DIR], TIMESTAMPS, results_plotter.X_TIMESTEPS, "DQN_CnnPolicy Boxing Over 5 million training cycles")
plt.show()
exit(0)

