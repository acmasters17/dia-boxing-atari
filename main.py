import gym
import time
from metricHandler import MetricHandler
from utilityFunctions import getAgentClass, parseCommandLineArguements

# Get settings for experiments that are passed as command line arguments
settings = parseCommandLineArguements()

# Get agent based off settings to use
chosenAgent = getAgentClass(settings.agentName)

# Get number of experiments based off settings used
numExperiments = int(settings.numberExperiments)

# Create the atari game environment and get a metrics Handler
env = gym.make('Boxing-v0', render_mode="human")
metricsHandler = MetricHandler()

# Can do a simple punching bot
# Can map observation space to actions like he did in lectures then run a ga - lecture on 22 march
# Crossover and mutation
for i in range(0, numExperiments):
    print("\nExperiment - ", i + 1)
    # Initialise Experiment Variables
    metricsHandler.startExperiment()
    runFinished = False

    env.reset()

    
    count = 0
    lastAction = 1
    while runFinished == False:
        # 18 different states for the action in boxing
        # 0 - do nothing - we want to throw fist then press zero to retract
        # 1 - throw fists and dont move      2 - move North
        # 3 - move East         4 - move West
        # 5 - move South         6 - move North East
        # 7 - move North West          8 - move South East
        # 9 - move South West
        # 10 - throw fist and move North           11 - throw fist and move East
        # 13 - throw fist and move South           14 - throw fists?
        # 15 - throw fists and move West 16 - throw fists and move East
        # 17

        if(count < 10):
            action = 3
        elif(count < 20):
            action = 5
        else:
            action = 13 if lastAction == 0 else 0
            lastAction = action

        count += 1
        observation, reward, done, info = env.step(chosenAgent.getAction(env))

        metricsHandler.updateScores(reward)
        runFinished = done

    # End experiment
    metricsHandler.endExperiment()

    print("Total Reward for Run: ", metricsHandler.getReward())
    print("Time in seconds of Run: ", metricsHandler.getExperimentTime())
    print("Player Score: ", metricsHandler.getAgentScore())
    print("Enemy Score: ", metricsHandler.getEnemyScore())

    env.close()
