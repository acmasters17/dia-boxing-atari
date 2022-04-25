from gym import Env
from Agents.Agent import Agent
from Models.Actions import BoxingAction

# principle for this approach is 
class JugglingReactiveAgent(Agent):
    def __init__(self):
        super().__init__()
        self.lastAction: BoxingAction = BoxingAction.NOOP
        self.firstHit = False
        self.midCombo = False

    def getAction(self,env:Env,lastobservation,lastreward):

        # intially if no hits registered we need to move towards opponent so go down right until we get a hit
        if(lastreward <= 0 and self.firstHit == False):
            newAction = self.downRightFireIntro()
            self.lastAction = newAction
            return newAction.value

        # if we get a hit then set first hit to true and make final move right
        if(lastreward > 0 and self.firstHit == False):
            self.firstHit = True
            self.lastAction = BoxingAction.MOVE_RIGHT
            return BoxingAction.MOVE_RIGHT.value
        
        # now we hit we want to bounce between fists
        newAction = self.juggleBetweenFists()
        self.lastAction = newAction
        return newAction.value

            
            

        

    # Moves Down Right / slowly into the middle while firing
    # alternates with NOOP so that fist retracts
    def downRightFireIntro(self):
        if(self.lastAction == BoxingAction.NOOP):
            return BoxingAction.FIRE_MOVE_DOWN_RIGHT
        else:
            return BoxingAction.NOOP


    # Tries to bounce fists via moving up and down and firing punches
    # Combo for this UF NOP DF NOP
    def juggleBetweenFists(self):

        if(self.lastAction == BoxingAction.MOVE_RIGHT):
            # First run so Fire upwards and start combo
            return BoxingAction.FIRE_MOVE_UP

        if(self.lastAction == BoxingAction.FIRE_MOVE_UP):
            self.midCombo = True
            return BoxingAction.NOOP
        elif(self.lastAction == BoxingAction.FIRE_MOVE_DOWN):
            self.midCombo = False
            return BoxingAction.NOOP
        else:
            # Last was NOOP so now need to return either FIRE UP MOVE or FIRE DOWN MOVE depending on state of combo
            if(self.midCombo == True):
                return BoxingAction.FIRE_MOVE_DOWN
            else:
                return BoxingAction.FIRE_MOVE_UP



   
