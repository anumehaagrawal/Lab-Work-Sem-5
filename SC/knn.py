import pandas as pd
def outcome(test,train,labels):
	summ=0
	arr =[]
	for j in range(len(train)):
		for i in range(len(test)):
			summ = summ+ (train[j][i]-test[i])**2
		summ = summ**(0.5)
		v=[]
		v.append(summ)
		v.append(train[j][-1])
		arr.append(v)
	arr =sorted(arr,key=lambda x:x[0])
	cz=0
	co=0
	for i in range(5):  # Set the value of k in knn
		if(arr[i][1]==0):
			cz=cz+1
		else:
			co=co+1
	if(co>cz):
		labels.append(1)
	else:
		labels.append(0)


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
	