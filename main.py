from simpleLinearRegression import SimpleLinearRegression
import tkinter
from tkinter import filedialog
import pandas
import matplotlib.pyplot
import decimal

# encapsulate in function to allow early returns
def RunRegression():
    
    # withdraw to hide tkinter window
    tkinter.Tk().withdraw()
    
    # open file explorer for user to select excel file
    filePath = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])

    # exit if no file
    if not filePath:
        return

    # use pandas for easy file reading
    data = pandas.read_excel(filePath)
    
    # format: x     y
    #         0.0   0.0
    #         0.0   0.0  etc.
    # in first and second column,
    # header is assumed, i.e. skips first row
    xPoints = data.iloc[:, 0].dropna().tolist() # ':' selects entire column 
    yPoints = data.iloc[:, 1].dropna().tolist() # dropna() removes empty cells

    # extract axis labels from file
    xLabel, yLabel = data.columns[[0, 1]]

    # place data into model
    try:
        model = SimpleLinearRegression(xPoints, yPoints)
    except Exception as exc:
        return
    
    # set up figure with dimensions
    figure, axes = matplotlib.pyplot.subplots(figsize=(8, 6))  
    
    # plot data points
    matplotlib.pyplot.scatter(xPoints, yPoints, label="Raw Data", color="blue")
    
    # create list of points y as a function of x for regression model
    xLine = [min(xPoints), max(xPoints)]
    yLine = [model.GetBeta_0() + model.GetBeta_1() * decimal.Decimal(xi) for xi in xLine]

    # plot regression line
    matplotlib.pyplot.plot(xLine, yLine, label="Regression Line", color="red")
    
    # add labels
    matplotlib.pyplot.xlabel(xLabel)
    matplotlib.pyplot.ylabel(yLabel)
    matplotlib.pyplot.legend()
    matplotlib.pyplot.title("Simple Linear Regression")

    # add info and stats to box
    infoText = (
        f"Model: yᵢ = {model.GetBeta_0():.6f} + {model.GetBeta_1():.6f}xᵢ\n"
        f"R²: {model.GetRSquared():.6f},\n"
        f"{model.GetRSquared() * 100:.1f}% of variance in data is explained by the model\n"
        f"Sample Correlation: {model.Getr():.6f}\n"
        f"σ² Estimate: {model.GetVarianceEstimate():.4f}\n"
        f"σ Estimate: {model.GetVarianceEstimate().sqrt():.4f}"
    )
    
    # leave space at bottom of window for info box
    figure.subplots_adjust(bottom=0.35)
    
    # place textbox  
    matplotlib.pyplot.figtext(0.15, # x position
            axes.get_position().ymin - 0.09, # y position - set from bottom of graph
            infoText, # text
            fontsize=12, # text size
            ha="left", # text horizontal alignment
            va="top", # text vertical alignment
            bbox=dict(facecolor="white")) # draw box background

    # show plot
    matplotlib.pyplot.show()

# run
RunRegression()

