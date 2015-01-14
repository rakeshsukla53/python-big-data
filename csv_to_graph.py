__author__ = 'rsukla'

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def graph():

    date, value = np.loadtxt('sampleCSV.csv', delimiter= ',', unpack= True,
                             converters= {0: mdates.strpdate2num('%Y-%m-%d')})

    fig = plt.figure()

    ax1 = fig.add_subplot(1,1,1, axisbg='white')

    plt.plot_date(x= date, y=value, fmt='-')

    plt.title('title')
    plt.ylabel('value')
    plt.xlabel('date')

    plt.show()

