import numpy as np
import math
import pandas as pd
class Perceptron:
	
	def __init__(self, input_size):
		self.W=np.array([1/(input_size+1) for i in range(input_size+1)])
		self.epochs=100
		self.alpha=0.9
		self.count=0

	def activation(self,x):
		ex = 1/(1+ math.exp(-1*abs(x)))
		
		if(ex>0.5):
			return 1
		return 0
		
	def predict(self,x):
		summ=0;
		for i in range(len(self.W)):
			temp=0
			for j in range(len(x)):
				temp = temp +self.W[i]*x[j]
			summ=summ+temp
		
		return self.activation(summ)

	def fit(self,X,Y):
		for j in range(self.epochs):
			for i in range(len(Y)):
				x = np.insert(X[i], 0, 1)
				y = self.predict(x)
				e = Y[i] - y		
				if(e==0 or e<0.00000000000000001):
					self.count=self.count+1
				self.W = self.W + self.alpha * e * x


df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
y = df.iloc[0:100, 4].values
Y = np.where(y == 'Iris-setosa', 0, 1)
X = df.iloc[0:100, [0, 2]].values
X=np.asarray(X)
Y=np.asarray(Y)

percep= Perceptron(input_size=2)


percep.fit(X, Y)
print("Accuracy is ")
print(percep.count/(len(Y)))
 
df_2 = pd.read_csv('spect1.csv')
y=df_2.iloc[0:80,0].values
X_2 = df_2.iloc[0:80, [i for i in range(1,44)]].values
X_2 =np.asarray(X_2)
y=np.asarray(y)

percep1= Perceptron(input_size=43)


percep1.fit(X_2, y)
print("Accuracy is ")
print(percep1.count/(len(y)))
