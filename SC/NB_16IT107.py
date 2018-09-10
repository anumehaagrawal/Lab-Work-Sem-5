import pandas as pd
import numpy as np
from collections import defaultdict
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


df = pd.read_csv('spect.csv')
df=df.values.tolist()
accuracy =0
recall=0
preci=0
count=0
for j in range(0,len(df)//20):
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

	tn=0
	fn=0
	tp=0
	fp=0
	for i in range(len(test)):
		if(labels[i]==0 and test[i][-1]==0):
			tn=tn+1
		elif(labels[i]==1 and test[i][-1]==1):
			tp=tp+1
		elif(labels[i]==1 and test[i][-1]==0):
			fp=fp+1
		else:
			fn=fn+1
	if(tp+fn !=0):
		rec= tp/(tp+fn)
		recall=recall+rec
	if(tp+fp !=0):
		prec = tp/(tp+fp)
		preci=preci+prec
	count=count+1
print("Accuracy is ", accuracy/count)
print("Precision is",preci/count)
print("Recall is",recall/count)