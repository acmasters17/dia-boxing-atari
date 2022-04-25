from typing import List
import matplotlib.pyplot as plt

# Draws a line graph of reward against experiment number
def drawRewardLineGraph(rewards:List[int]):
    # plotting the rewards
    plt.plot(rewards, label = "Rewards")
    plt.xlabel('x - Number of Experiments')
    # Set the y axis label of the current axis.
    plt.ylabel('y - Total Reward')
    # Set a title of the current axes.
    plt.title('Graph of Total Reward Across Experiments ')
    # show a legend on the plot
    plt.legend()
    # Display a figure.
    plt.show()