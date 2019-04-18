import math
import io
import csv
from array import *
import matplotlib.pyplot as plt

#this reads the csv file in
with open("holeData.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
 
    xCoord = []
    yCoord = []

    radius = []

    arr1875 = []
    arr25 = []
    arr3125 = []
    arr375 = []
    arr4375 = []
    arr5 = []

    for row in readCSV:
        

        x = float(row[0])
        y = float(row[1])
        r = float(row[2])
    
        xCoord.append(x)
        yCoord.append(y)
        radius.append(r)

    plt.plot(xCoord,yCoord,'bo')
    plt.show()
