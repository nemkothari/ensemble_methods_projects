# %load q01_bagging/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

plt.switch_backend('agg')
# Data Loading
dataframe = pd.read_csv('data/loan_prediction.csv')

X = dataframe.iloc[:, :-1]
y = dataframe.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

def bagging(X_train,X_test,y_train,y_test,n_est):
    np.random.seed(9)
    # Fitting bagging classifier with Logisitc Regression
    bagging_clf2 = BaggingClassifier(DecisionTreeClassifier(), n_estimators=n_est, max_samples=67, 
                                bootstrap=True, random_state=9)
    bagging_clf2.fit(X_train, y_train)
    y_pred = bagging_clf2.predict(X_train)
    
    y_pred_bagging = bagging_clf2.predict(X_test)
    score_bc_dt = accuracy_score(y_test, y_pred_bagging)
    score_bc = accuracy_score(y_train, y_pred)
    
    return  score_bc,score_bc_dt
    
xaxis = range (1,51)
yaxis = []
zaxis = []
for i in range (1,51):
    a,b = bagging(X_train,X_test,y_train,y_test,i)
    yaxis.append(a)
    zaxis.append(b)
    
plt.plot(xaxis,yaxis,c='blue')
plt.plot(xaxis,zaxis , c ='red')
plt.show()


