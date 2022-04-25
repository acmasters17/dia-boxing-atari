import gym
from matplotlib import pyplot as plt
from Graphs.playerVsEnemyScoreLineGraph import drawPlayerVsEnemyScoreLineGraph
from Scoring.metricHandler import MetricHandler
from Utilities.utilityFunctions import getAgentClass, getIsSilent, getNumberOfExperiments, getShouldDisplay, parseCommandLineArguements
import random

plt.style.use('seaborn-deep')

# Get settings for experiments that are passed as command line arguments
settings = parseCommandLineArguements()

# Get agent based off settings to use
chosenAgent = getAgentClass(settings.agentName)

# Get number of experiments based off settings used
numExperiments = getNumberOfExperiments(settings.numberExperiments)

# Get if program should be silent or not
isSilent = getIsSilent(settings.isSilent)

# Get if proram should render or not
shouldDisplay = getShouldDisplay(settings.shouldDisplay)

# Create the atari game environment and get a metrics Handler
env = gym.make('Boxing-v0', render_mode="human") if shouldDisplay else gym.make('Boxing-v0')
# Set the seed of the runs
random.seed(0)
env.seed(0)
metricsHandler = MetricHandler()



# Can do a simple punching bot
# Can map observation space to actions like he did in lectures then run a ga - lecture on 22 march
# Crossover and mutation
for i in range(0, numExperiments):
    print("\nExperiment - ", i + 1)

    # Initialise Experiment Variables
    metricsHandler.createNewExperiment()
    metricsHandler.startCurrentExperiment()
    runFinished = False

    observation = env.reset()
    reward = 0

    while runFinished == False:
        newobs, newreward, done, info = env.step(chosenAgent.getAction(env,observation,reward))

        observation = newobs
        reward = newreward

        metricsHandler.updateScoresForCurrentExperiment(newreward)

        runFinished = done

    # End experiment
    metricsHandler.endCurrentExperiment()

    # Print out current experiment results
    if isSilent == False:
        metricsHandler.printCurrentExperimentResults()


    # Log current experiment
    metricsHandler.logCurrentExperiment()

    env.close()


# Log out results of all experiments 
print("*************************\n")
print("RESULTS")
print("-------------------------")
print("Number of KO Wins: ", metricsHandler.getNumberOfKOWins())
print("Number of Wins: ", metricsHandler.getNumberOfWins())
print("Number of Draws: ", metricsHandler.getNumberOfDraws())
print("Number of Losses: ", metricsHandler.getNumberOfLosses())
print("Number of KO Losses: ", metricsHandler.getNumberOfKOLosses())
print("\n")
print("AVERAGES")
print("-------------------------")
print("Average Reward for " + str(numExperiments) + " experiments: ", metricsHandler.getAverageReward())
print("Average Player Score for " + str(numExperiments) + " experiments: ",metricsHandler.getAveragePlayerScore())
print("Average Enemy Score for " + str(numExperiments) + " experiments: ",metricsHandler.getAverageEnemyScores())
print("Average Number of Actions for " + str(numExperiments) + " experiments: ",metricsHandler.getAverageNumberOfActionsTaken())
print("Average Experiment Real Time seconds for " + str(numExperiments) + " experiments: ",metricsHandler.getAverageNumberOfRealTimeSeconds())
print("Average Win Rate for " + str(numExperiments) + " experiments: ", metricsHandler.getAverageWinRate(), "%")
print("\n")

# Display graphs
experiments = metricsHandler.getAllExperiments()

# Draw a line graph of scores
# drawPlayerVsEnemyScoreLineGraph(playerscores=[ e.getAgentScore() for e in experiments], enemyscores=[ e.getEnemyScore() for e in experiments])



