import math
import io
import csv
from array import *
import matplotlib.pyplot as plt

#this reads the csv file in
with open("holeData.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')

    xCoord = []
    yCoord = []
    radius = []

    x1875 = []
    y1875 = []
    x25 = []
    y25 = []
    x3125 = []
    y3125 = []
    x375 = []
    y375 = []
    x4375 = []
    y4375 = []
    x5 = []
    y5 = []

    for row in readCSV:

        x = float(row[0])
        y = float(row[1])
        r = float(row[2])

        if(r==0.1875):
            x1875.append(x)
            y1875.append(y)
            plt.plot(x1875, y1875, 'r*')
            #radius.append(r)
        elif(r==0.25):
            x25.append(x)
            y25.append(y)
            plt.plot(x25, y25, 'b*')
        elif(r==0.3125):
            x3125.append(x)
            y3125.append(y)
            plt.plot(x3125, y3125, 'y*')
        elif(r==0.375):
            x375.append(x)
            y375.append(y)
            plt.plot(x375, y375, 'g*')
        elif(r==0.4375):
            x4375.append(x)
            y4375.append(y)
            plt.plot(x4375, y4375, 'b.')
        elif(r==0.5):
            x5.append(x)
            y5.append(y)
            plt.plot(x5, y5, 'r.')
        
        
        
    
        #xCoord.append(x)
        #yCoord.append(y)
        #radius.append(r)

    #plt.plot(xCoord,yCoord,'bo')
    plt.show()
