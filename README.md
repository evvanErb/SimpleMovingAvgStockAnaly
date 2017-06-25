# SimpleMovingAvgStockAnaly

Simple graphing of moving averages from .csv file 
Will request in terminal how long ago you would like the graph to start

Please make sure .csv is formated like this:

"date","close","volume","open","high","low"
"16:00","153.26","25.762.799","153.63","153.94","152.11"
"2017/05/10","153.2600","25779060.0000","153.6300","153.9400","152.1100"
"2017/05/09","153.9900","38907940.0000","153.8700","154.8800","153.4500"
"2017/05/08","153.0100","48670440.0000","149.0300","153.7000","149.0300"

You can download in this format from:
http://www.nasdaq.com/quotes/historical-quotes.aspx

But make sure that in the second line commas are only outside double quotes and periods inside (example: "233.445",)

Takes data from file named stockData.csv and writes data to stockAnalyzed.csv

Dependecies: Python 2.7, numpy, pandas, matplotlib

For best results run program from terminal (python MovingAvg.py)

Make sure stockData.csv is in same directory as MovingAvg.py

README contains example files for stockData.csv and stockAnalyzed.csv
