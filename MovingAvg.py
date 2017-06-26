#!/usr/bin/python2

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

#creating data frame
stockData = pd.DataFrame(lines[2:],columns = lines[0])
priceData = stockData["close"]

#creating 10 point medians and adding to end of dataframe
mediansTEN = []
for point in range(len(priceData)):
	median = 0.0
	total = 10.0
	for i in range(10):
		try:
			median += float(priceData[point+i])
		except:
			total -= 1
	mediansTEN.append(median/total)
stockData["mediansTEN"] = pd.Series(mediansTEN, index=stockData.index)

#creating 20 point medians and adding to end of dataframe
mediansTWENTY = []
for point in range(len(priceData)):
	median = 0.0
	total = 20.0
	for i in range(20):
		try:
			median += float(priceData[point+i])
		except:
			total -= 1
	mediansTWENTY.append(median/total)
stockData["mediansTWENTY"] = pd.Series(mediansTWENTY, index=stockData.index)

#creating 50 point medians and adding to end of dataframe
mediansFIFTY = []
for point in range(len(priceData)):
	median = 0.0
	total = 50.0
	for i in range(50):
		try:
			median += float(priceData[point+i])
		except:
			total -= 1
	mediansFIFTY.append(median/total)
stockData["mediansFIFTY"] = pd.Series(mediansFIFTY, index=stockData.index)

#creating 100 point medians and adding to end of dataframe
mediansHUNDRED = []
for point in range(len(priceData)):
	median = 0.0
	total = 100.0
	for i in range(100):
		try:
			median += float(priceData[point+i])
		except:
			total -= 1
	mediansHUNDRED.append(median/total)
stockData["mediansHUNDRED"] = pd.Series(mediansHUNDRED, index=stockData.index)


#creating 200 point medians and adding to end of dataframe
mediansTWOHUND = []
for point in range(len(priceData)):
	median = 0.0
	total = 200.0
	for i in range(200):
		try:
			median += float(priceData[point+i])
		except:
			total -= 1
	mediansTWOHUND.append(median/total)
stockData["mediansTWOHUNDRED"] = pd.Series(mediansTWOHUND, index=stockData.index)

#Writing analyzed data to file
filename = "stockAnalyzed.csv"
stockData.to_csv(filename, index=False, encoding='utf-8')

#*****Visualizing Data*****

#See how many days ago user wants to see
goodVal = True
while(goodVal):
	howLong = int(raw_input("How many days ago do you want the graph to start?\n>>> "))
	if(howLong >= len(priceData)):
		print("There is no data for that long ago. Enter a new value.")
		goodVal = True
	else:
		goodVal = False

#OLD CODE FROM v1.0 STILL REWORKING

# #Original
# maxPrice = 0
# plots = []
# for i in range((len(ser)-howLong), len(ser)):
# 		plots.append(float(ser[i]))		
# plt.plot(plots, 'red')
# maxPrice = max(plots)

# #10MA
# plots = []
# for i in range((len(ser)-howLong), len(mediansTEN)):
# 		plots.append(float(mediansTEN[i]))
# plt.plot(plots, 'orange')

# #20MA
# plots = []
# for i in range((len(ser)-howLong), len(mediansTWENTY)):
# 		plots.append(float(mediansTWENTY[i]))
# plt.plot(plots, 'yellow')

# #50MA
# plots = []
# for i in range((len(ser)-howLong), len(mediansFIFTY)):
# 		plots.append(float(mediansFIFTY[i]))
# plt.plot(plots, 'green')

# #100MA
# plots = []
# for i in range((len(ser)-howLong), len(mediansHUNDRED)):
# 		plots.append(float(mediansHUNDRED[i]))
# plt.plot(plots, 'blue')

# #200MA
# plots = []
# for i in range((len(ser)-howLong), len(mediansTWOHUND)):
# 		plots.append(float(mediansTWOHUND[i]))
# plt.plot(plots, 'purple')

# plt.ylabel('Price')
# plt.xlabel('Day')
# plt.title('Stock Moving Avgerages')
# plt.text(0, maxPrice, 'Red = Original : Orange = 10MA : Yellow = 20MA : Green = 50MA : Blue = 100MA : Purple = 200MA')
# plt.show()