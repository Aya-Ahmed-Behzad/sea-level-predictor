import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv('epa-sea-level.csv')
    # Perform linear regression for the first dataset
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(1880, 2051)
    
    # Predicting values from year 1880 till year 2050
    predicted1 = slope1 * years + intercept1
    
    df2= df.loc[df['Year'] >= 2000.0]   
    # Perform linear regression for the second dataset
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level'])
    
    years2 = np.arange(2000, 2051)
    
    # Predicting values from year 2000 till year 2050
    predicted2 = slope2 * years2 + intercept2
    
    # Plotting the data and the regression lines
    #creating the scatter plot 
    graph= df.plot.scatter('Year', 'CSIRO Adjusted Sea Level', color='blue', label='Data')
    graph.axis(xmax = 2070, ymax = 18)
    
    # plotting first line of best fit
    graph.plot(years, predicted1, color='orange', label='Line of Best Fit1')
    
    # plotting second line of best fit
    graph.plot(years2, predicted2, color='red', linestyle='--',label='Line of Best Fit2')
    
    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(loc=2)
    plt.grid()
           
    # Save plot and return data for testing 
    plt.savefig('sea_level_plot.png')
    return plt.gca()
