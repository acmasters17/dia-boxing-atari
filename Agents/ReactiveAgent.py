from gym import Env
from Agents.Agent import Agent

# principle for this approach is 
class ReactiveAgent(Agent):
    def __init__(self):
        super().__init__()

    def getAction(self,env:Env,lastobservation,lastreward):
        print(lastreward)
        return 0