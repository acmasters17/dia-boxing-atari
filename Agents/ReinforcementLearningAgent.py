import random
from gym import Env
from stable_baselines3 import A2C
from Agents.Agent import Agent
from stable_baselines3 import ACER

# Agent will load best model
class ReinforcementLearningAgent(Agent):
    def __init__(self):
        super().__init__()
        self.model = ACER.load("./TrainingInfo/models/A2C_CnnPolicy/model_at_1000000")
    def getAction(self,env:Env,lastobservation,lastreward):
        action, _states = self.model.predict(lastobservation, deterministic=True)
        return action