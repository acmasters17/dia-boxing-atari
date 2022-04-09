from typing import List
import matplotlib.pyplot as plt

# Draws a line graph with player score vs enemy score on it 
def drawPlayerVsEnemyScoreLineGraph(playerscores:List[int] ,enemyscores:List[int]):
    # plotting the player points 
    plt.plot(playerscores, label = "Player Scores")
    # plotting the enemy points
    plt.plot(enemyscores, label = "Enemy Scores")
    plt.xlabel('x - Number of Experiments')
    # Set the y axis label of the current axis.
    plt.ylabel('y - Scores')
    # Set a title of the current axes.
    plt.title('Graph of Scores Across Experiments ')
    # show a legend on the plot
    plt.legend()
    # Display a figure.
    plt.show()


