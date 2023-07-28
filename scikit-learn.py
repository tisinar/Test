import pandas as pd
import numpy as np

iris=r['iris']
df=pd.DataFrame(iris)
X_iris= df.drop('Species',axis=1)
Y_iris=df['Species']
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,mean_squared_error


Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, Y_iris,random_state=1)

model = GaussianNB() # 2. instantiate model
model.fit(Xtrain,ytrain) # 3. fit model to data
y_model = model.predict(Xtest)
accuracy_score(ytest,y_model)
confusion_matrix(ytest,y_model)
mean_squared_error(ytest,y_model)






