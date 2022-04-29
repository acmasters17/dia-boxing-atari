import random
from gym import Env
from stable_baselines3 import A2C
from Agents.Agent import Agent

# Agent will load best model
class ReinforcementLearningAgent(Agent):
    def __init__(self):
        super().__init__()
        self.model = A2C.load("./TrainingInfo/models/A2C_CnnPolicy/model_at_100000")
    def getAction(self,env:Env,lastobservation,lastreward):
        action, _states = self.model.predict(lastobservation, deterministic=True)
        return action