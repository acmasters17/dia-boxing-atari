import random
from gym import Env
import gym
from Agents.Agent import Agent
from stable_baselines3 import A2C, PPO
from Utilities.modelSaver import SaveOnBestTrainingRewardCallback

# Agent will train using reinforment learning
class ReinforcementLearningAgent(Agent):
    def __init__(self):
        super().__init__()
        CHECKPOINT_DIR = './train/'
        LOG_DIR = './logs/'
        callback = SaveOnBestTrainingRewardCallback(check_freq=10000,save_path=CHECKPOINT_DIR)
        env = gym.make('Boxing-v0')
        random.seed(0)
        env.seed(0)
        model = A2C("MlpPolicy", env, verbose=1, tensorboard_log=LOG_DIR)
        model.learn(total_timesteps=100000, callback=callback)
        exit(0)
        # self.model = model

    def getAction(self,env:Env,lastobservation,lastreward):
        action, _states = self.model.predict(lastobservation, deterministic=True)
        return action