# Model for an experiment
import time
from Models.Results import Result


class ExperimentMetrics:
    def __init__(self):
        # Initialise an experiment class
        self.agentScore = 0
        self.enemyScore = 0
        self.startTime = 0
        self.endTime = 0
        self.numOfActions = 0
        self.result = Result.UNKNOWN
    
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

    # Ends expirment and sets end time and if win or not
    def endExperiment(self):
        self.endTime = time.time()

        if(self.agentScore == 100):
            self.result = Result.KOWIN
        elif(self.enemyScore == 100):
            self.result = Result.KOLOSS
        elif(self.agentScore > self.enemyScore):
            self.result = Result.WIN
        elif(self.enemyScore > self.agentScore):
            self.result = Result.LOSS
        elif(self.agentScore == self.enemyScore):
            self.result = Result.DRAW
        else:
            print("ERROR Unknown Result")
            self.result = Result.UNKNOWN

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

    # returns result of experiment
    def getExperimentResult(self):
        return self.result

    # prints results
    def printExperimentResults(self):
        print("Total Reward for Run: ", self.getReward())
        print("Real Time in seconds of Run: ", self.getExperimentTime())
        print("Number of Action Loops: ",self.getNumberOfActionsTaken())
        print("Player Score: ", self.getAgentScore())
        print("Enemy Score: ", self.getEnemyScore())
        print("Result: ", self.getExperimentResult().name)
    
