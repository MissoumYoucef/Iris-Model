import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
import random

from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("iris\iris.csv")
nb_row, nb_col = df.shape
#print(nb_row, nb_col)
#print(df.sample(frac=0.25))

def scale_dataset(dataframe, oversample=False):
  X = dataframe[dataframe.columns[:-1]].values
  y = dataframe[dataframe.columns[-1]].values

  scaler = StandardScaler()
  X = scaler.fit_transform(X)

  if oversample:
    ros = RandomOverSampler()
    X, y = ros.fit_resample(X, y)

  data = np.hstack((X, np.reshape(y, (-1, 1))))

  return data, X, y

#train, valid, test = np.split(df.sample(frac=1), [int(0.7*len(df)), int(0.71*len(df))])
X = df[df.columns[:-1]].values
y = df[df.columns[-1]].values
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
#train, test = np.split(df.sample(frac=1), [int(0.7*len(df))])

#train, x_train, y_train = scale_dataset(train, oversample=False)
#valid, x_valid, y_valid = scale_dataset(valid, oversample=False)
#test, x_test, y_test = scale_dataset(test, oversample=False)

# ## SVM

def svm():
    svm_model = SVC(kernel='linear', )
    svm_model = svm_model.fit(x_train, y_train)
    y_pred = svm_model.predict(x_test)
    #return classification_report(y_test, y_pred)
    return accuracy_score(y_test, y_pred)


#SVC(kernel='rbf') => accuracy = 0.9, 0.96(False)
#SVC(kernel='linear') => accuracy = 0.93, 0.88(False)
#SVC(kernel='poly') => accuracy = 0.83, 0.97(False)
#SVC(kernel='sigmoid') => accuracy = 0.9, 0.86(False)

#if we modify % of dataset in train and test, it modify the accuracy


# ## Log Regression
def LogRegression():
    from sklearn.linear_model import LogisticRegression
    lg_model = LogisticRegression()
    lg_model = lg_model.fit(x_train,y_train)
    y_pred = lg_model.predict(x_test)
    return classification_report(y_test,y_pred)