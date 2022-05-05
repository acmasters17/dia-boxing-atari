
import matplotlib.pyplot as plt
from Scoring.metricHandler import MetricHandler

# Draws a Bar Chart showing percentage of experiemtns that were wins losses etc
def drawResultsBarChart(metricsHandler: MetricHandler):
    labels = ["KOWins", "Wins", "Draws", "Losses", "KOLosses"]
    results = [metricsHandler.getNumberOfKOWins(), metricsHandler.getNumberOfWins(), metricsHandler.getNumberOfDraws(), metricsHandler.getNumberOfLosses(), metricsHandler.getNumberOfKOLosses()]
    plt.bar(x=labels,height=results)
    # Set a title of the current axes.
    plt.title('Bar Chart Of Results ')
    # show a legend on the plot
    plt.legend(title="Result Types:")
    # Display a figure.
    plt.show()