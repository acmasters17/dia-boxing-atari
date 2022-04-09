# Model for an experiment
import time


class ExperimentMetrics:
    def __init__(self):
        # Initialise an experiment class
        self.agentScore = 0
        self.enemyScore = 0
        self.startTime = 0
        self.endTime = 0
        self.numOfActions = 0
    
    # Updates scores in experiment based off reward
    # if score has happened then action has been taken as well
    def updateScores(self,reward:float):
        self.numOfActions += 1
        if reward >= 1:
            self.agentScore += reward
        elif reward <= -1:
            self.enemyScore += -reward
        else:
            return

    # Sets time for current Experiment
    def startExperiment(self):
        self.startTime = time.time()

    # Ends expirment and sets end time
    def endExperiment(self):
        self.endTime = time.time()

    # Returns player score / num of hits
    def getAgentScore(self):
        return self.agentScore
    
    # Returns enemy score / num of hits taken
    def getEnemyScore(self):
        return self.enemyScore

    # Returns current reward - this is difference in scores
    def getReward(self):
        return self.agentScore - self.enemyScore

    # returns how long the expirment was running / this tends to only work in human render mode
    def getExperimentTime(self):
        return round(self.endTime - self.startTime)

    # returns number of actions taken
    def getNumberOfActionsTaken(self):
        return self.numOfActions

    # prints results
    def printExperimentResults(self):
        print("Total Reward for Run: ", self.getReward())
        print("Time in seconds of Run: ", self.getExperimentTime())
        print("Player Score: ", self.getAgentScore())
        print("Enemy Score: ", self.getEnemyScore())
    
