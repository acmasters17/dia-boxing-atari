import matplotlib.pyplot as plt
from Scoring.metricHandler import MetricHandler


# Draws a Pie Chart showing percentage of experiemtns that were wins losses etc
def drawResultsPieChart(metricsHandler: MetricHandler):
    labels = ["KOWins", "Wins", "Draws", "Losses", "KOLosses"]
    results = [metricsHandler.getNumberOfKOWins(), metricsHandler.getNumberOfWins(), metricsHandler.getNumberOfDraws(), metricsHandler.getNumberOfLosses(), metricsHandler.getNumberOfKOLosses()]
    plt.pie(results,labels=labels)
    # Set a title of the current axes.
    plt.title('Pie Chart Of Results ')
    # show a legend on the plot
    plt.legend(title="Result Types:")
    # Display a figure.
    plt.show()
