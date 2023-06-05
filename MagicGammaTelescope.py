import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import classification_report

# https://archive.ics.uci.edu/ml/datasets/magic+gamma+telescope

# Use Case:
cols = ["fLength", "fWidth", "fSize", "fConc", "fConcl", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
magicDf = pd.read_csv("magic04.data", names=cols)
magicDf["class"] = (magicDf["class"] == "g").astype(int)

# for label in cols[:-1]:
#     plt.hist(magicDf[magicDf["class"] == 1][label], color ='blue', label= 'gamma', alpha = 0.7, density = True)
#     plt.hist(magicDf[magicDf["class"] == 0][label], color ='red', label= 'hadron', alpha = 0.7, density = True)
#     plt.title(label)
#     plt.ylabel("Probability")
#     plt.xlabel(label)
#     plt.legend()
#     plt.show()

# train, validate and test data sets

train, valid, test = np.split(magicDf.sample(frac=1), [int(0.6*len(magicDf)), int(0.8*len(magicDf))])
# print(magicDf.head())

def scale_dataset(dataframe,oversample = False):

    X = dataframe[dataframe.columns[:-1]].values

    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    if oversample:
        ros = RandomOverSampler()
        X,y = ros.fit_resample(X,y)

    data = np.hstack((X,np.reshape(y,(-1,1))))

    return data,X ,y

train, X_train,y_train = scale_dataset(train,oversample = True)
valid, X_valid,y_valid = scale_dataset(valid,oversample = False)
test, X_test,y_test = scale_dataset(test,oversample = False)
#print(X_test.dtype)

#KNN
from sklearn.neighbors import KNeighborsClassifier

knn_model = KNeighborsClassifier(n_neighbors=1)

knn_model.fit(X_train,y_train)

y_pred = knn_model.predict(X_test)
print (classification_report(y_test,y_pred))

#Naive Bayes
from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()
nb_model = nb_model.fit(X_train,y_train)

y_pred = nb_model.predict(X_test)
print(classification_report(y_test,y_pred))

#Logistic Regression
from sklearn.linear_model import LogisticRegression
lg_model = LogisticRegression()
lg_model = nb_model.fit(X_train,y_train)

y_pred = lg_model.predict(X_test)
print(classification_report(y_test,y_pred))

#Support Vector Machine (SVM)
from sklearn.svm import SVC
svm_model = SVC()
svm_model = svm_model.fit(X_train,y_train)

y_pred = svm_model.predict(X_test)
print(classification_report(y_test,y_pred))

#Neural Net

import tensorflow as tf

def plot_history(history):
  fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,4))
  ax1.plot(history.history['loss'], label='loss')
  ax1.plot(history.history['val_loss'], label='val_loss')
  ax1.set_xlabel('Epoch')
  ax1.set_ylabel('Binary Crossentropy Loss')
  ax1.legend()
  ax1.grid(True)

  ax2.plot(history.history['accuracy'], label='accuracy')
  ax2.plot(history.history['val_accuracy'], label='val_accuracy')
  
  ax2.set_xlabel('Epoch')
  ax2.set_ylabel('Accuracy')
  ax2.grid(True)

  plt.show()

#plot_history(history)

# def plot_accuracy(history):
#   plt.plot(history.history['accuracy'], label='accuracy')
#   plt.plot(history.history['val_accuracy'], label='val_accuracy')
#   plt.title('Model Accuracy')
#   plt.xlabel('Epoch')
#   plt.ylabel('Accuracy')
#   plt.legend()
#   plt.grid(True)
#   plt.show()

#Grid Search logic is added.
def train_model(X_train,y_train,num_nodes,dropout_prob,lr,batch_size,epochs):
  nn_model = tf.keras.Sequential([
    tf.keras.layers.Dense(num_nodes,activation = 'relu',input_shape = (10,)),
    tf.keras.layers.Dropout(dropout_prob),
    tf.keras.layers.Dense(num_nodes,activation = 'relu'),
    tf.keras.layers.Dropout(dropout_prob),
    tf.keras.layers.Dense(1,activation = 'sigmoid')
  ])

  nn_model.compile(optimizer= tf.keras.optimizers.Adam(lr),loss = 'binary_crossentropy',
                  metrics=['accuracy'])

  history = nn_model.fit(
    X_train,y_train, epochs=epochs, batch_size=batch_size, validation_split = 0.2,verbose=0)
  return nn_model,history

#Gridsearch
least_val_loss = float('inf') #Initialized to infinity so that any model is covered
least_loss_model = None
epochs = 100
#for num_nodes in [16,32,64]:
#for dropout_prob in [0,0.2]:
#for lr in [0.01,0.005,0.001]:
#for batch_size in [32,64,128]:

for num_nodes in [16]:
   for dropout_prob in [0]:
      for lr in [0.01]:
         for batch_size in [32]:
          print(f"{num_nodes} nodes,dropout {dropout_prob},lr {lr}, batch size {batch_size}")
          model,history =  train_model(X_train,y_train,num_nodes, dropout_prob, lr,batch_size,epochs)
          
          plot_history(history)
          
                  
          val_loss = model.evaluate(X_valid,y_valid)[0]
          if val_loss < least_val_loss:
             least_val_loss = val_loss
             least_loss_model = model
y_pred = least_loss_model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int).reshape(-1,)
print(classification_report(y_test,y_pred))

#Comparing the classification report SVM is working out little better although not much of a difference




