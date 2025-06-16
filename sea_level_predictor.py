import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')

    # Create scatter plot
    plt.subplots(figsize=(15,8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color = 'green')
    plt.ylim(-2,15)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extended_Year = np.arange(df['Year'].min(), df['Year'].max() + 40)
    extended_sea_level = slope * extended_Year + intercept

    extended_df = pd.DataFrame({'Year': extended_Year, 'CSIRO Adjusted Sea Level':extended_sea_level })
    plt.plot(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(extended_df['Year'], extended_df['CSIRO Adjusted Sea Level'], 'r--')
    
    
    # Create second line of best fit
    Year_x = np.arange(2000,2051)
    extended_y = slope * Year_x + intercept 
    plt.plot(Year_x, extended_y, color='black')


    # Add labels and title
    plt.xlabel('Year', fontsize = 14)
    plt.ylabel('Sea Level (inches)',fontsize=14)
    plt.title('Rise in Sea Level', fontsize=20)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()