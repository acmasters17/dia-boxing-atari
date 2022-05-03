from gym import Env
from Agents.Agent import Agent

# Agent will load best model passed to it then use it to make predictions
class ReinforcementLearningAgent(Agent):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def getAction(self,env:Env,lastobservation,lastreward):
        action, _states = self.model.predict(lastobservation, deterministic=True)
        return action