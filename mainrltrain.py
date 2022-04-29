import os
import random
import gym
from matplotlib import pyplot as plt
from Utilities.modelSaver import SaveOnBestTrainingRewardCallback
# from stable_baselines3.common.env_util import make_atari_env
# from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common import results_plotter
from stable_baselines3 import A2C
from stable_baselines3.common.results_plotter import plot_results
from stable_baselines3.common.monitor import Monitor




# So this is going to the model training main that is used to train RL algorithms
# When run it will train a reinforcement learning model based of input parameters
CHECKPOINT_DIR = './TrainingInfo/'
LOCAL_LOGS_DIR = './TrainingInfo/local_logs'
TENSORBOARD_LOGS_DIR = './TrainingInfo/tensorboard_logs/'
TIMESTAMPS = 50000
os.makedirs(LOCAL_LOGS_DIR, exist_ok=True)
callback = SaveOnBestTrainingRewardCallback(check_freq=1000,save_path=CHECKPOINT_DIR, algorithm_name="A2C_MlpPolicy")
env = gym.make('Boxing-v0')
random.seed(0)
env.seed(0)
env = Monitor(env, LOCAL_LOGS_DIR)
model = A2C("MlpPolicy", env, verbose=1, tensorboard_log=TENSORBOARD_LOGS_DIR)
model.learn(total_timesteps=TIMESTAMPS, callback=callback)

plot_results([LOCAL_LOGS_DIR], TIMESTAMPS, results_plotter.X_TIMESTEPS, "A2C Boxing")
plt.show()
exit(0)

