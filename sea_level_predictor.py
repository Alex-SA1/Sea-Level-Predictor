import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv', sep=',', header='infer')

    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    first_line = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    x_extended = np.arange(df.iloc[0]['Year'].astype('float64'), 2051, 1)

    y_line = first_line.intercept + first_line.slope * x_extended

    plt.plot(x_extended, y_line, color='red')

    second_line = linregress(x=df[df['Year'] >= 2000]['Year'],
                             y=df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])

    x_modified = np.arange(2000, 2051, 1)

    y_line = second_line.intercept + second_line.slope * x_modified

    plt.plot(x_modified, y_line, color='yellow')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()
