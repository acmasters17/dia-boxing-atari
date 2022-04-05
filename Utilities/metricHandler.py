import time

class MetricHandler:
    def __init__(self):
        # Initialise
        self.agentScore = 0
        self.enemyScore = 0
        self.startTime = 0
        self.endTime = 0

    def updateScores(self,reward:float):
        if reward >= 1:
            self.agentScore += reward
        elif reward <= -1:
            self.enemyScore += -reward
        else:
            return

    
    def startExperiment(self): 
        self.agentScore = 0
        self.enemyScore = 0
        self.startTime = time.time()
        self.endTime = 0
    
    def endExperiment(self):
        self.endTime = time.time()

    def getAgentScore(self):
        return self.agentScore
    
    def getEnemyScore(self):
        return self.enemyScore

    def getReward(self):
        return self.agentScore - self.enemyScore

    def getExperimentTime(self):
        return round(self.endTime - self.startTime)

