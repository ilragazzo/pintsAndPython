import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math

#############################################################################
#Author: Tony Sanchez
#Last edited: 10-14-2018
#Last editor: Tony Sanchez
#Description:
#This function generates FAKED data in the same format that's used in Plot.py
#use this f(x) gen to check the accuracy of your algorithms agaist functions 
#that can be easily verrified.
# 
#The API returns real data in the format :
#symbol,open,high,low,price,volume,latestDay,previousClose,change,changePercent
#getStock.py adds a date-time stamp at the end of our real data
#
#This appends a value of x at the end that DOES NOT appear in real data
#############################################################################

#open a file  named GenData.txt
file ='GenData.txt'
out = open(file,"w")

#makes arrays
Dates=[]
Prices=[]
x=0
PreMarket=10
Market=390
MarketPad=10 # give a few extra to allow for a constant price at close
# make up some data
for x in range(-PreMarket,Market+MarketPad):
     
     if x>=0 and x<Market:
          #sets the date stamp for the test signal data
          date = (datetime.datetime.utcnow() + datetime.timedelta(seconds =x)).strftime("%H:%M:%S")
     
          #your test signal function goes here:
          y=100000 - ((25*x*math.cos(x/math.pi))-x**(3)/390 + x**(2)-x   )

          if y > 0:
               price = y
          
          if y < 0:
               price = 0     
          
          
          Dates.append(date)
          Prices.append(price) 
     
          out.write("symbl,open,high,low, ")
          out.write(str(price)+", vol,Day,prevCls,diff,diff%, ")
          out.write(str(date)+", ")
          out.write(str(x)+ "\n") # for trace tables
     
     if x<0 :
          price=0
          date = (datetime.datetime.utcnow() + datetime.timedelta(seconds =x)).strftime("%H:%M:%S")
          Dates.append(date)
          Prices.append(price)
          out.write("symbl,open,high,low, ")
          out.write(str(price)+", vol,Day,prevCls,diff,diff%, ")
          out.write(str(date)+", ")
          out.write(str(x)+ "\n") # for trace tables
          
     if x>Market:
          price = price
          date = (datetime.datetime.utcnow() + datetime.timedelta(seconds =x)).strftime("%H:%M:%S")
          Dates.append(date)
          Prices.append(price)
          out.write("symbl,open,high,low, ")
          out.write(str(price)+", vol,Day,prevCls,diff,diff%, ")
          out.write(str(date)+", ")
          out.write(str(x)+ "\n") # for trace tables
     
    
# plot
plt.plot([],[])
plt.scatter(Dates,Prices,s=8)
# beautify the x-labels
plt.gcf().autofmt_xdate()


#print (Dates)
#print (Prices)

plt.show()
out.close()


