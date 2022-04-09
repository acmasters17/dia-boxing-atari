import time

from Scoring.experimentMetrics import ExperimentMetrics

class MetricHandler:
    def __init__(self):
        # Initialise
        self.currentExperiment = ExperimentMetrics()
        self.experimentsMetricsList = []

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




