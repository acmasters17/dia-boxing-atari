from typing import List

from Scoring.experimentMetrics import ExperimentMetrics

class MetricHandler:
    def __init__(self):
        # Initialise
        self.currentExperiment = ExperimentMetrics()
        self.experimentsMetricsList:List[ExperimentMetrics] = []

    def updateScoresForCurrentExperiment(self,reward:float):
        self.currentExperiment.updateScores(reward)

    
    def startCurrentExperiment(self): 
        self.currentExperiment.startExperiment()
    
    def endCurrentExperiment(self):
        self.currentExperiment.endExperiment()

    

    def printCurrentExperimentResults(self):
        self.currentExperiment.printExperimentResults()

    def logCurrentExperiment(self):
        self.experimentsMetricsList.append(self.currentExperiment)

    def createNewExperiment(self):
        self.currentExperiment = ExperimentMetrics()

    def getAllExperiments(self):
        return self.experimentsMetricsList

    def getAverageReward(self):
        rewards = [ e.getReward() for e in self.experimentsMetricsList]
        return sum(rewards) / len(rewards)

    def getAveragePlayerScore(self):
        playerScores = [ e.getAgentScore() for e in self.experimentsMetricsList]
        return sum(playerScores) / len(playerScores)

    def getAverageEnemyScores(self):
        enemyScores = [ e.getEnemyScore() for e in self.experimentsMetricsList]
        return sum(enemyScores) / len(enemyScores)

    def getAverageNumberOfActionsTaken(self):
        numActioms = [ e.getNumberOfActionsTaken() for e in self.experimentsMetricsList]
        return sum(numActioms) / len(numActioms)

    def getAverageNumberOfRealTimeSeconds(self):
        numSeconds = [ e.getExperimentTime() for e in self.experimentsMetricsList]
        return sum(numSeconds) / len(numSeconds)
    


    
        




