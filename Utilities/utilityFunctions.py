from argparse import ArgumentParser
from Agents.Agent import Agent

from Agents.RandomAgent import RandomAgent

# Parses command line arguments to get settings for program
def parseCommandLineArguements():
    parser = ArgumentParser()
    parser.add_argument("-a", dest="agentName",
                    help="Agent name to run experiments for - random, srs, ga, rl", metavar="Agent", required=True, choices=["random", "srs", "ga", "rl"])
    parser.add_argument("-n", dest="numberExperiments", help="Number of experiments to run e.g 100 ", metavar="Num of Runs", default=10)
    # parser.add_argument("-q", "--quiet",
    #                     action="store_false", dest="verbose", default=True,
    #                     help="don't print status messages to stdout")

    args = parser.parse_args()

    return args


# Get agent class based off argument
def getAgentClass(name):
    if(name == "random"):
        return RandomAgent()
    else:
        return Agent()