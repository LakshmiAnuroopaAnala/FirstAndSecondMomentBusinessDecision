# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#FIRST DATA SCIENCE APPLICATION DAY 1 11/5/2020
#MEAN MEDIAN MODE
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

salaries=pd.read_csv("E:/SalaryDetails.csv")
meanValue=salaries.salary.mean()
medianValue=salaries.days.median()
modeValue=salaries.salary.mode()
print("Mean is",meanValue)
print("Median value is",medianValue)
print("Mode value is",modeValue)

#SECOND DATA SCIENCE APPLICATION DAY 2 12/5/2020
#VARIANCE STANDARD DEVIATION RANGE
varianceValue=salaries.salary.var()
stdevValue=salaries.days.std()
range=max(salaries.days)-min(salaries.days)
print("Variance is",varianceValue)
print("Standard Deviation is",stdevValue)
print("Range value is",range)

#BAR GRAPH

plt.bar(height=salaries.days,x=salaries.sno)

#HISTOGRAPH
plt.hist(salaries.sno)
plt.hist(salaries.days)

#BOX PLOT TO INDENTIFY THE OUTLIER 
value1=plt.boxplot(salaries.sno)


