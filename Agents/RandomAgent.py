from gym import Env
from Agents.Agent import Agent

# Agent will randomly select an action from the sample space and return that action
class RandomAgent(Agent):
    def __init__(self):
        super().__init__()

    def getAction(self, env:Env):
        return env.action_space.sample()
