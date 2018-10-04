import pandas as pd
import numpy as np
from collections import defaultdict
from random import randint
import collections
population=[]
highest_accuracy=[]
best_features=[]
def priori(df):
	count=0
	c_out=0
	for i in df:
		if(i[-1]==0):
			c_out=c_out+1
		count=count+1
	zero= c_out/count
	one =1-zero
	d ={}
	d[0]=zero
	d[1]=one
	return d

def posterior(df):
	feature_imp = []
	rows = len(df)
	cols = len(df[0])-1
	classes=[0,1]
	for i in classes:
		cl = []
		for j in range(cols):
			cn=0
			cp=0
			for k in df:
				if (k[j]==0 and k[-1]==i):
					cn=cn+1
				elif (k[j]==1 and k[-1]==i):
					cp=cp+1
			d={}
			p=priori(df)
			d[0]= cn/(p[i]*rows)
			d[1] =cp/(p[i]*rows)
			cl.append(d)
		feature_imp.append(cl)
	return feature_imp

def outcome(row,df,labels):
	feature_imp = posterior(df)
	results={}
	class_p = priori(df)
	classes=[0,1]
	for i in classes:
		cp_i = class_p[i]
		for j in range(0,len(row)-1):
			relative_vals = feature_imp[i][j]
			cp_i *= relative_vals[row[j]]
			if(cp_i != 0):
				results[i] = cp_i
	if(results[0]>results[1]):
		labels.append(0)
	else:
		labels.append(1)

def model_cv(features=None):
	df = pd.read_csv('spect.csv')
	if(features==None):
		df=df.values.tolist()
	else:
		arr=[]
		for i in range(len(features)):
			if(features[i]==0):
				arr.append(i)
		df=df.drop(df.columns[arr], axis=1) 
		df=df.values.tolist()
	
	accuracy =0
	recall=0
	preci=0
	count=0
	for j in range(0,len(df)//20):
		count=count+1
		test=df[j*20:(j+1)*20]
		train=df[0:j*20]+df[(j+1)*20:len(df)]

		labels=[]
		for i in range(len(test)):
			outcome(test[i],train,labels)
		c=0
		for i in range(len(test)):
			if(labels[i]==test[i][-1]):
				c=c+1
		accuracy=accuracy+ c/20*100

	return accuracy/count

def initialize_features(num):
	population.clear()
	for j in range(9):
		arr=[0]*num
		n=randint(1, num-1)
		for i in range(n):
			index=randint(0,9)
			arr[index]=1
		population.append(arr)
	return population	

def selection(population):
	parents=[]
	o = randint(0,len(population)-1)
	t= randint(0,len(population)-1)
	parents.append(population[o])
	parents.append(population[t])
	return parents

def crossover(parents):
	length = len(parents[0])
	cross_over=randint(1,length-1)
	children=[]
	for i in range(cross_over,length):
		temp=parents[0][i]
		parents[0][i]=parents[1][i]
		parents[1][i]=temp
	children.append(parents[0])
	children.append(parents[1])
	return children

def mutation(children):
	length = len(children[0])
	mut=randint(0,length-1)
	for i in children:
		if(i[mut]==0):
			i[mut]=1
		else:
			i[mut]=0
	for i in children:
		population.append(i)

main_accuracy = model_cv()
pop = initialize_features(22)
for i in range(1000):
	parents=selection(population)
	child= crossover(parents)
	mutation(child)

	accuracy_array=[]
	for i in population:
		acc = model_cv(i)
		accuracy_array.append(acc)
	dict_pop={}
	for i in range(len(accuracy_array)):
		dict_pop[accuracy_array[i]]=population[i]
	od = collections.OrderedDict(sorted(dict_pop.items()))
	i=0
	
	for key,value in od.items():
		if(i==len(od)-1):
			highest_accuracy.append(key)
			best_features.append(value)		
		i=i+1
	
print(highest_accuracy)