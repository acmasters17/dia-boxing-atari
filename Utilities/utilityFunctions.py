from argparse import ArgumentParser

from Agents.Agent import Agent
from Agents.RandomAgent import RandomAgent
from Agents.AggressiveJugglingReactiveAgent import AggressiveJugglingReactiveAgent
from Agents.DefensiveJugglingReactiveAgent import DefensiveJugglingReactiveAgent
from Agents.ReinforcementLearningAgent import ReinforcementLearningAgent

# Parses command line arguments to get settings for program
def parseCommandLineArguements():
    parser = ArgumentParser()
    parser.add_argument("-a", dest="agentName",
                        help="Agent name to run experiments for - random, ajugglingBot, djugglingBot, ga, rl", metavar="Agent", required=True, choices=["random", "ajugglingBot", "djugglingBot", "ga", "rl"])
    parser.add_argument("-n", dest="numberExperiments",
                        help="Number of experiments to run e.g 100 ", metavar="Num of Runs", default=10)
    parser.add_argument("-s", dest="isSilent", metavar="Is Silent", default=False,
                        help="don't print experiment status messages to stdout")
    parser.add_argument("-d", dest="shouldDisplay", metavar="Display Screen", default=False,
                        help="render what is happening in the game")

    args = parser.parse_args()

    return args


# Get agent class based off argument
def getAgentClass(name: str):
    if(name == "random"):
        return RandomAgent()
    elif(name == "ajugglingBot"):
        return AggressiveJugglingReactiveAgent()
    elif(name == "djugglingBot"):
        return DefensiveJugglingReactiveAgent()
    elif(name == "rl"):
        return ReinforcementLearningAgent()
    else:
        return Agent()


# Get number of experiments based off argument if less than 1 return 1
def getNumberOfExperiments(n: str):
    num = int(n)
    if(num < 1):
        print("Error in number of experiments passed, must be greater than or equal to 1")
    else:
        return num


# Gets if it should output logging messages or not
def getIsSilent(s: str):
    if(s == "True"):
        return True
    else:
        return False

# Gets if it should display the screen as the boxing takes place
def getShouldDisplay(s: str):
    if(s == "True"):
        return True
    else:
        return False
