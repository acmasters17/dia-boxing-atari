import random
from gym import Env
from Agents.Agent import Agent


# Agent will load model that is input
class ReinforcementLearningAgent(Agent):
    def __init__(self):
        super().__init__()
        
        # self.model = model

    def getAction(self,env:Env,lastobservation,lastreward):
        action, _states = self.model.predict(lastobservation, deterministic=True)
        return action