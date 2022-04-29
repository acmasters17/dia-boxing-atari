import random
from gym import Env
from Agents.Agent import Agent
from Models.Actions import BoxingAction

# principle for this approach is 
class TestAgent(Agent):
    def __init__(self):
        super().__init__()
        self.lastAction: BoxingAction = BoxingAction.NOOP
        self.firstHit = False
        self.midCombo = False
        self.delayCounter = 0
        self.deadlockCounter = 0
        self.nextDirection = BoxingAction.NOOP

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
        newAction = self.juggleBetweenFists(lastreward)
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
    def juggleBetweenFists(self, reward):

        # Count how many times reward is zero in a row
        if(reward == 0):
            self.deadlockCounter += 1
        else:
            self.deadlockCounter = 0


        # If we get hit at any point step backwards
        if(reward < 0):
            self.midCombo = False

        if(self.midCombo == False):
            # Start Roping Combo by 50 50 FUR or FDR
            self.midCombo = True
            # Get Combo Staring Varient
            comboVariant = BoxingAction.FIRE_MOVE_UP_RIGHT if random.randint(0,1) == 0 else BoxingAction.FIRE_MOVE_DOWN_RIGHT
            # Update next direction for next punch
            self.nextDirection = BoxingAction.FIRE_MOVE_DOWN if comboVariant == BoxingAction.FIRE_MOVE_UP_RIGHT else BoxingAction.FIRE_MOVE_UP
            return comboVariant
        elif(self.lastAction == BoxingAction.FIRE_MOVE_UP_RIGHT or self.lastAction == BoxingAction.FIRE_MOVE_DOWN_RIGHT):
            # Now we have fired a punch and started combo so return a NOOP
            return BoxingAction.NOOP
        elif(self.lastAction == BoxingAction.NOOP or wasMovementOperation(self.lastAction)):
            # mid combo and just had nop so throw a punch in next direction 
            if(self.nextDirection == BoxingAction.FIRE_MOVE_DOWN):
                if(self.delayCounter > 0):
                    self.delayCounter -= 1
                    return BoxingAction.NOOP
                self.nextDirection = BoxingAction.FIRE_MOVE_UP
                return BoxingAction.FIRE_MOVE_DOWN
            else:
                if(self.delayCounter > 0):
                    self.delayCounter -= 1
                    return BoxingAction.NOOP
                self.nextDirection = BoxingAction.FIRE_MOVE_DOWN
                return BoxingAction.FIRE_MOVE_UP
        else:
            # Now we want to move forward if we didnt score with a punch as probably far away but if did score then stay in same place
            if(reward > 0):
                self.delayCounter = 5
                return BoxingAction.NOOP
                return BoxingAction.MOVE_DOWN if self.nextDirection == BoxingAction.FIRE_MOVE_DOWN else BoxingAction.MOVE_UP
            else:
                if(self.deadlockCounter >= 10):
                    # Been in a deadlock so move back and fire
                    self.deadlockCounter = 0
                    return BoxingAction.FIRE_MOVE_DOWN_LEFT if self.nextDirection == BoxingAction.FIRE_MOVE_DOWN else BoxingAction.FIRE_MOVE_UP_LEFT
                else:
                    # we want to move foward as missed punch
                    return BoxingAction.MOVE_RIGHT
            


# returns if movement operation or fire operation
def wasMovementOperation(action: BoxingAction):
    if(action == BoxingAction.MOVE_DOWN or action == BoxingAction.MOVE_DOWN_RIGHT or action == BoxingAction.MOVE_UP or action == BoxingAction.MOVE_UP_RIGHT or action == BoxingAction.MOVE_RIGHT or action == BoxingAction.MOVE_LEFT):
        return True
    else:
        return False


   
