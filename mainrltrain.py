import os
import random
import gym
from matplotlib import pyplot as plt
import numpy as np
from Utilities.modelSaver import SaveOnBestTrainingRewardCallback
from stable_baselines3.common import results_plotter
from stable_baselines3 import A2C, TD3
from stable_baselines3.common.results_plotter import plot_results
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.noise import NormalActionNoise




# So this is going to the model training main that is used to train RL algorithms
# When run it will train a reinforcement learning model based of input parameters
CHECKPOINT_DIR = './TrainingInfo/'
LOCAL_LOGS_DIR = './TrainingInfo/local_logs'
TENSORBOARD_LOGS_DIR = './TrainingInfo/tensorboard_logs/'
TIMESTAMPS = 100000
os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
callback = SaveOnBestTrainingRewardCallback(check_freq=1000,save_path=CHECKPOINT_DIR, algorithm_name="TD3_MlpPolicy")
env = gym.make('Boxing-v0')
random.seed(0)
env.seed(0)
env = Monitor(env, LOCAL_LOGS_DIR)
# Add some action noise for exploration
n_actions = env.action_space.shape[-1]
action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.1 * np.ones(n_actions))
# Because we use parameter noise, we should use a MlpPolicy with layer normalization
model = TD3('MlpPolicy', env, action_noise=action_noise, verbose=0, tensorboard_log=TENSORBOARD_LOGS_DIR)
# model = A2C("MlpPolicy", env, verbose=1, tensorboard_log=TENSORBOARD_LOGS_DIR)
model.learn(total_timesteps=TIMESTAMPS, callback=callback)

plot_results([LOCAL_LOGS_DIR], TIMESTAMPS, results_plotter.X_TIMESTEPS, "TD3-MlpPolicy Boxing")
plt.show()
exit(0)

