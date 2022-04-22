from gym import Env
import gym
from Agents.Agent import Agent
from stable_baselines3 import A2C, PPO

# Agent will train using reinforment learning
class ReinforcementLearningAgent(Agent):
    def __init__(self):
        super().__init__()
        env = gym.make('Boxing-v0')
        model = A2C("MlpPolicy", env, verbose=1)
        model.learn(total_timesteps=10000)
        self.model = model

    def getAction(self,env:Env,lastobservation,lastreward):
        action, _states = self.model.predict(lastobservation, deterministic=True)
        return action