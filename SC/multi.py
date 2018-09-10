import pandas as pd
import numpy as np
class NeuralNet:
	def __init__(self,input_size):
		self.input_size=input_size
		self.hidden=1;
		self.epochs=100
		self.W= [1/(input_size+1) for i in range(input_size+1)]
		self.W=np.asarray(self.W)
		self.W_h = [1/6 for i in range(6)]
		self.W_h=np.asarray(self.W_h)
		
	def forward_prop(self,X):



df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
y = df.iloc[0:100, 4].values
Y = np.where(y == 'Iris-setosa', 0, 1)
X = df.iloc[0:100, [0, 2]].values
X=np.asarray(X)
Y=np.asarray(Y)
print(X[0])
nn = NeuralNet(len(X[0]))