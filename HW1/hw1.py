#Raymond Dao
#CSCI 5502
#HW1

#1. To use, run python from command line: 'python hw1.py'
#2. You will be prompted for two integer values i and j corresponding to columns
#3. Results will be printed to command line

import sys
import csv
import numpy as np

	
	
def metric(i,j):
	assert i >=0 and i<14
	assert j >=0 and j<14
	
	col_labels = ["per capita crime rate by town", \
				  "proportion of residential land zoned",\
				  "proportion of non-retail business acres per town",\
				  "Charles River dummy variable",\
				  "nitric oxides concentration",\
				  "average number of rooms per dwelling",\
				  "proportion of owner-occupied units built prior to 1940",\
				  "weighted distances to five Boston employment centres",\
				  "index of accessibility to radial highways",\
				  "full-value property-tax rate per $10,000",\
				  "pupil-teacher ratio by town",\
				  "1000(Bk - 0.63)^2 where Bk is the proportion of blacks",\
				  "% lower status of the population",\
				  "Median value of owner-occupied homes in $1000's"]
					
	
	#Load the data
	filename = "housing.data.txt"
	d = []
	data = np.loadtxt(filename,skiprows=0)
	length =len(data);
	
	#Grab N, min, max, mean, std for col-i
	current_i = []
	for x in range(0,length):
		current_i.append(data[x][i])
	
	i_N = len(current_i)	
	i_min = min(current_i)
	i_max = max(current_i)
	i_mean = np.mean(current_i)
	i_std = np.std(current_i)
	
	#Grab Q1, median, Q3, IQR for col-j
	current_j = []
	for y in range(0,length):
		current_j.append(data[y][j])
		
	q75, q25 = np.percentile(current_j, [75 ,25])
	
	j_q1 = q25
	j_median = np.median(current_j)
	j_q3 = q75
	j_iqr = q75 - q25
	
	#Print the values
	#for the i data
	print 'For column i='+str(i)+': '+col_labels[i]
	print 'Minimum: '+str(i_min)
	print 'Maximum: '+str(i_max)
	print 'Mean: '+str(i_mean)
	print 'Standard Deviation: '+str(i_std)
	
	print '------------------------------------------------'
	
	#for the j data
	print 'For column j='+str(j)+': '+col_labels[j]
	print 'Q1: '+str(j_q1)
	print 'Median: '+str(j_median)
	print 'Q3: '+str(j_q3)
	print 'IQR: '+str(j_iqr)
	
#######################

i = raw_input("Type in integer column for i: ")
j = raw_input("Type in integer column for j: ")
metric(int(i),int(j))
