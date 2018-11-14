# -*- coding: utf-8 -*-

##############################################
#Author: Tony Sanchez
#last edited: 10-14-2018
#last edited by: Tony Sanchez
#
#
#Description:
# This file will apply algorithims to data
# 
##Goals#
#  open file for reading
#  read stock price data  
#  format data from string to float
#  apply a derivative algorithm
#  
##############################################
import numpy
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
import csv 


file = "GenData.txt"    #stock + "parsedStockData.txt"

Stash = 0
Investment =0
Bankroll = 100

shares = 1
maxShares = 1 #maximum amout of shares to be bought

PurchPrice =0.5 # average shareprice?
HoldPrice =0 
HiPrice =0 
LowPrice = 10**100 
lastprice =0

StopLoss = True
maxLoss = 2

sold = False


with open (file) as csvfile:
     readcsv =csv.reader(csvfile,delimiter=',')
     Dates=[]
     Prices=[]
     slopes=[]
     slopes.append(0) #artifact of finding a point between 2 ponits
     m=0
     n=0
          
             
     #for loop starts here
     for row in readcsv:
          
          #gets the date from Row 7 and price from Row 5
          PriceStr = row[4]
          Price = float(PriceStr)
          DateStr = row[11]
          Date = float(DateStr)
          Prices.append(Price)
          Dates.append(Date)
          #print (Date)
          
          fox = Prices[n]
          
          if n>=1:
               
               fox_1 = Prices[n-1]
               dt = -1
               m = (fox_1-fox)/dt
               slopes.append(m)
               #print ("Price:",Price)
               #print ("Prices: ", Prices[-2])
               #print (slope)
          
          #print ("x = ",n," f(x) = ",fox," slope", m)
          #for loop control:
          n=n+1
          
          if shares > 0: # If you have shares then you ride the market
               if Price > PurchPrice:
                    if Price > HiPrice:
                         HiPrice = Price
                         HoldPrice = Price
                         Investment = shares*Price
               
               if Price < HoldPrice and m < 0:
                    if StopLoss == True :
                         if (HoldPrice -Price) > maxLoss:
                              shares = shares -1
                              sold = True
                              Investment =shares*Price
                              Bankroll = Bankroll + Price
                              print ("sell")
                              
                              
          if shares < maxShares:
               if Price < HoldPrice or PurchPrice:
                    LowPrice = Price
                    if m >0 and (Bankroll - Price)> 0: 
                         print ("buy") 
                         Bought =True
                         shares = shares + 1
                         Bankroll = Bankroll - Price
                         Investment = shares*Price 
                         PurchPrice = Price
                    
                                   
                         
          
          
          
          
          print ( "%.2f" % Price,"%.2f"  % Investment,"%.2f" % Bankroll)#, "%.2f" % LowPrice)
                       
print("%.2f" % (Bankroll + Investment), "%.2f" % HiPrice,"%.2f" % LowPrice)
# plot
plt.plot([],[])
plt.scatter(Dates,Prices,s=8,c="b")
plt.scatter(Dates,slopes,s=8,c="r")


# beautify the x-labels
plt.gcf().autofmt_xdate()


#print (Dates)
#print (Prices)

plt.show()

