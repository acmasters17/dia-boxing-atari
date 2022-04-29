from matplotlib import pyplot as plt
from Utilities.modelSaver import SaveOnBestTrainingRewardCallback
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack
from stable_baselines3.common import results_plotter
from stable_baselines3 import A2C
from stable_baselines3.common.results_plotter import plot_results




# So this is going to the model training main that is used to train RL algorithms
# When run it will train a reinforcement learning model based of input parameters
CHECKPOINT_DIR = './TrainingInfo/train/'
LOG_DIR = './TrainingInfo/logs/'
TIMESTAMPS = 20000
callback = SaveOnBestTrainingRewardCallback(check_freq=5000,save_path=CHECKPOINT_DIR)
# There already exists an environment generator
# that will make and wrap atari environments correctly.
# Here we are also multi-worker training (n_envs=4 => 4 environments)
env = make_atari_env('BoxingNoFrameskip-v4', n_envs=4, seed=0)
# Frame-stacking with 4 frames
env = VecFrameStack(env, n_stack=4)
model = A2C("MlpPolicy", env, verbose=1, tensorboard_log=LOG_DIR)
model.learn(total_timesteps=TIMESTAMPS, callback=callback)

plot_results([LOG_DIR], TIMESTAMPS, results_plotter.X_TIMESTEPS, "A2C Boxing")
plt.show()
exit(0)

