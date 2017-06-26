#!/usr/bin/python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("[*] Program reading and analyzing data")

#Import data and store each line as list
data = open("stockData.csv", "r")
lines = data.readlines()

#split into 2d array
for item in range(len(lines)):
	lines[item] = lines[item].split(",")
	
#remove extraneous commas and endlines
for item in lines:
	for i in range(len(item)):
		item[i] = item[i].replace("\n","")
		item[i] = item[i].replace(",","")
		item[i] = item[i].replace("\"","")

#creating series for points and medians
arr = np.array(lines[1:])
ser = pd.Series(arr[:,1], range(len(arr),0,-1))
mediansTEN = pd.Series(arr[:,1], range(len(arr),0,-1))
mediansTWENTY = pd.Series(arr[:,1], range(len(arr),0,-1))
mediansFIFTY = pd.Series(arr[:,1], range(len(arr),0,-1))
mediansHUNDRED = pd.Series(arr[:,1], range(len(arr),0,-1))
mediansTWOHUND = pd.Series(arr[:,1], range(len(arr),0,-1))

#Turning 10 point medians to medians series
for point in range(len(ser), 0, -1):
	median = 0.0
	total = 10.0
	for i in range(10):
		try:
			median += float(ser[point-i])
		except:
			total -= 1
	mediansTEN[point] = (median/total)

#Turning 20 point medians to medians series
for point in range(len(ser), 0, -1):
	median = 0.0
	total = 20.0
	for i in range(20):
		try:
			median += float(ser[point-i])
		except:
			total -= 1
	mediansTWENTY[point] = (median/total)

#Turning 50 point medians to medians series
for point in range(len(ser), 0, -1):
	median = 0.0
	total = 50.0
	for i in range(50):
		try:
			median += float(ser[point-i])
		except:
			total -= 1
	mediansFIFTY[point] = (median/total)

#Turning 100 point medians to medians series
for point in range(len(ser), 0, -1):
	median = 0.0
	total = 100.0
	for i in range(100):
		try:
			median += float(ser[point-i])
		except:
			total -= 1
	mediansHUNDRED[point] = (median/total)


#Turning 200 point medians to medians series
for point in range(len(ser), 0, -1):
	median = 0.0
	total = 200.0
	for i in range(200):
		try:
			median += float(ser[point-i])
		except:
			total -= 1
	mediansTWOHUND[point] = (median/total)


#Writing analyzed data to file
output = open("stockAnalyzed.csv", "w")
mediansSTR = ""
mediansSTR += "Day,Price,10MA,20MA,50MA,100MA,200MA\n"
for i in range(len(mediansTEN), 0, -1):
	mediansSTR += (str(i) + "," + str(ser[i]) + "," + str(mediansTEN[i]) + "," + str(mediansTWENTY[i]) + "," + str(mediansFIFTY[i]) + "," + str(mediansHUNDRED[i]) + "," + str(mediansTWOHUND[i]) + "\n")
	
output.write(mediansSTR)
output.close()

#*****Visualizing Data*****

#See how many days ago user wants to see
goodVal = True
while(goodVal):
	howLong = int(raw_input("How many days ago do you want the graph to start?\n>>> "))
	if(howLong >= len(ser)):
		print("There is no data for that long ago. Enter a new value.")
		goodVal = True
	else:
		goodVal = False

#Original
maxPrice = 0
plots = []
for i in range((len(ser)-howLong), len(ser)):
		plots.append(float(ser[i]))		
plt.plot(plots, 'red')
maxPrice = max(plots)

#10MA
plots = []
for i in range((len(ser)-howLong), len(mediansTEN)):
		plots.append(float(mediansTEN[i]))
plt.plot(plots, 'orange')

#20MA
plots = []
for i in range((len(ser)-howLong), len(mediansTWENTY)):
		plots.append(float(mediansTWENTY[i]))
plt.plot(plots, 'yellow')

#50MA
plots = []
for i in range((len(ser)-howLong), len(mediansFIFTY)):
		plots.append(float(mediansFIFTY[i]))
plt.plot(plots, 'green')

#100MA
plots = []
for i in range((len(ser)-howLong), len(mediansHUNDRED)):
		plots.append(float(mediansHUNDRED[i]))
plt.plot(plots, 'blue')

#200MA
plots = []
for i in range((len(ser)-howLong), len(mediansTWOHUND)):
		plots.append(float(mediansTWOHUND[i]))
plt.plot(plots, 'purple')

plt.ylabel('Price')
plt.xlabel('Day')
plt.title('Stock Moving Avgerages')
plt.text(0, maxPrice, 'Red = Original : Orange = 10MA : Yellow = 20MA : Green = 50MA : Blue = 100MA : Purple = 200MA')
plt.show()
