from gym import Env
from Agents.Agent import Agent
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation

# Agent will randomly select an action from the sample space and return that action
class ReinforcementLearningAgent(Agent):
    def __init__(self, env:Env):
        super().__init__()
        height, width, channels = env.observation_space.shape
        actions = env.action_space.n

    def getAction(self, env:Env):
        return env.action_space.sample()