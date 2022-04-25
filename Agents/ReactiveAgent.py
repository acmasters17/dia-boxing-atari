from gym import Env
from Agents.Agent import Agent

# principle for this approach is 
class ReactiveAgent(Agent):
    def __init__(self):
        super().__init__()
        self.lastAction = "DR"
        self.firstHit = False

    # ['NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'DOWN', 
    #  'UPRIGHT', 'UPLEFT', 'DOWNRIGHT', 'DOWNLEFT', 
    #  'UPFIRE', 'RIGHTFIRE', 'LEFTFIRE', 'DOWNFIRE', 
    #  'UPRIGHTFIRE', 'UPLEFTFIRE', 'DOWNRIGHTFIRE', 'DOWNLEFTFIRE']
    def getAction(self,env:Env,lastobservation,lastreward):

        # intially if no hits registered we need to move towards opponent so go down right until we get a hit
        if(lastreward <= 0 and self.firstHit == False):
            return self.downRightFireIntro()

        # if we get a hit then set first hit to true and make final move right
        if(lastreward > 0 and self.firstHit == False):
            self.firstHit = True
            self.lastAction = "R"
            return 3
        
        # now we hit we want to bounce between fists

            
            

        

    # Moves Down Right / slowly into the middle while firing
    def downRightFireIntro(self):
        if(self.lastAction == "DR"):
            self.lastAction = "DRF"
            return 16
        if(self.lastAction == "DRF"):
            self.lastAction = "DR"
            return 0


    # Tries to bounce fists via moving up and down and firing punches
    # Combo for this UF NOP DF NOP
    def juggleBetweenFists(self):
        if(self.lastAction == "R"):
            # First run so UF
            self.lastAction = "UF"
            return 5

        elif(self.lastAction == "D"):

            # Fire Down
            self.lastAction = "DF"
            return 13

        elif(self.lastAction == "DF"):

            # Move Up
            self.lastAction = "U"
            return 2

        else:

            # Fire Up
            self.lastAction = "UF"
            return 10



   
