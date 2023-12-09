# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 21:29:02 2023

@author: gameb
"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report, confusion_matrix
###############################################################################
# Question 1 prep to test things
###############################################################################
# raw_data = pd.read_csv('A4_Part2_Data_MaxwellSolko.csv')
# df_labels = raw_data['LABEL'] #putting the labels in a separate series 
# df_labels = df_labels.to_numpy()
# df = raw_data.drop('LABEL', axis=1) #getting the data in a separate copy
# df = (df-df.min())/(df.max()-df.min()) #min-max scaling
# print(df)
# X = df.to_numpy()
# y = df_labels.copy().reshape((len(X),1))
# ###################### Creating one hot labels for y ------------------
# y_copy = y.copy()
# temp = y
# #print(temp)
# one_hot_labels = np.zeros((len(X), 3))
# #print(one_hot_labels)
# for i in range(len(X)):
#     one_hot_labels[i, temp[i]] = 1    
# #print(one_hot_labels)
# y = one_hot_labels
# #print(" Y is\n", y)
###############################################################################
# Question 1
###############################################################################
ANN_Model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(4, input_shape=(4,), activation = 'sigmoid'),
    tf.keras.layers.Dense(3, activation = 'relu'),
    tf.keras.layers.Dense(3, activation = 'softmax')
    ])

ANN_Model.summary()

ANN_Model.compile(
    loss='categorical_crossentropy',
    metrics = ['accuracy']
    )

# epoch_history = ANN_Model.fit(X, y, 
#                               epochs =10
#                               )
# plt.plot(epoch_history.history['accuracy'], label='Accuracy')

###############################################################################
# Question 2
###############################################################################
CNN_Model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(filters=2, kernel_size=(3,3), input_shape=(30,30,1), 
                           activation = 'relu', padding='same'),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(filters=4, kernel_size=(3,3), 
                           activation='relu', padding='same'),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(3, activation = 'softmax')
    ])

CNN_Model.summary()

CNN_Model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.01),
    loss='sparse_categorical_crossentropy',
    metrics = ['accuracy']
    )




###############################################################################
# Question 3
###############################################################################
raw_data = pd.read_csv('Final_News_DF_Labeled_ExamDataset.csv') #Make sure you have the working directory to where this is!
df_labels = raw_data['LABEL'] #putting the labels in a separate series 
df_labels = df_labels.to_numpy()
df = raw_data.drop('LABEL', axis=1) #getting the data in a separate copy
# df = (df-df.min())/(df.max()-df.min()) #min-max scaling
print(df)
X = df.to_numpy()
y = df_labels.copy().reshape((len(X),1))

def MakeLabelsNumeric(labels): 
    # If there are only two labels then it will be binary
    lbls = np.unique(labels)
    temp = labels.copy()
    print(lbls)
    for i in range(len(lbls)):
        temp[temp == lbls[i]] = i
    return temp
###################### Creating one hot labels for y ------------------
y_copy = y.copy() #if I want original labels
temp = MakeLabelsNumeric(y)
#print(temp)
temp = np.ndarray.astype(temp, int) #for the for loop, indices can't be object type
one_hot_labels = np.zeros((len(X), 3))
#print(one_hot_labels)


for i in range(len(y)):
    one_hot_labels[i, temp[i]] = 1    
#print(one_hot_labels)
y = one_hot_labels
#print(" Y is\n", y)


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

print("Input Example:", x_train[0])
print("Label Example:", y_train[0])

print("Shape of x_train:",x_train.shape)
print("Shape of x_test:",x_test.shape)
print("Shape of y_train:",y_train.shape)
print("Shape of y_test:",y_test.shape)


# np.sum(y_train, axis=0) #398 of label 0, 403 of label 1, 292 of label 2. 
# np.sum(y_test, axis=0) #102 of label 0, 94 of label 1, 103 of label 2. 

##############################For visuals
def make_confusion_matrix(confusion_matrix):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.matshow(confusion_matrix, cmap=plt.cm.Blues, alpha=0.3)
    for i in range(confusion_matrix.shape[0]):
        for j in range(confusion_matrix.shape[1]):
            ax.text(x=j, y=i,s=confusion_matrix[i, j], va='center', ha='center', size='xx-large')
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix for LSTM', fontsize=18)
    # plt.locator_params(axis='x', nbins=12)
    # plt.locator_params(axis='y', nbins=12)
    lbls = [0] + ['football', 'politics', 'science'] #Need an extra entry at the start to line up right
    ax.xaxis.set_ticklabels(lbls, fontsize = 18)
    ax.yaxis.set_ticklabels(lbls, fontsize = 18)
    plt.show()
#####################################



ANN_Model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(20, input_shape=(300,), activation = 'relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation = 'relu'),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(3, activation = 'softmax')
    ])

ANN_Model.summary()

ANN_Model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics = ['accuracy']
    )



epoch_historyANN = ANN_Model.fit(x_train, y_train, 
                              epochs =200, 
                              validation_data=(x_test, y_test) 
                              )

plt.plot(epoch_historyANN.history['accuracy'], label='Accuracy')
plt.plot(epoch_historyANN.history['val_accuracy'])
plt.title("Accuracy of the ANN Model")
plt.show()

y_pred = ANN_Model.predict(x_test)
y_pred = y_pred.argmax(axis=1)
y_test_labels = y_test.argmax(axis=1)
cnf_matrix_auth = confusion_matrix(y_test_labels, y_pred)
# print(classification_report(y_test_labels, y_pred))
#make a nicer figure for the confusion matrix
make_confusion_matrix(cnf_matrix_auth)

###############################################################################

CNN_Model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(20, kernel_size=5, input_shape=(300,1), activation = 'relu'),
    tf.keras.layers.Conv1D(10, kernel_size=3, activation = 'relu'),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(3, activation = 'softmax')
    ])

CNN_Model.summary()

CNN_Model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics = ['accuracy']
    )



epoch_historyCNN = CNN_Model.fit(x_train, y_train, 
                              epochs =200, 
                              validation_data=(x_test, y_test) 
                              )

plt.plot(epoch_historyCNN.history['accuracy'], label='Accuracy')
plt.plot(epoch_historyCNN.history['val_accuracy'])
plt.title("Accuracy of the CNN Model")
plt.show()

y_pred = CNN_Model.predict(x_test)
y_pred = y_pred.argmax(axis=1)
y_test_labels = y_test.argmax(axis=1)
cnf_matrix_auth = confusion_matrix(y_test_labels, y_pred)
# print(classification_report(y_test_labels, y_pred))
#make a nicer figure for the confusion matrix
make_confusion_matrix(cnf_matrix_auth)

###############################################################################

LSTM_Model = tf.keras.models.Sequential([
    tf.keras.layers.LSTM(30, input_shape=(300,1), dropout=0.1),
    # tf.keras.layers.LSTM(20, dropout=0.1), #need return_sequences=True in previous layer if you use this
    tf.keras.layers.Dense(3, activation='softmax')])

LSTM_Model.summary()

LSTM_Model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics = ['accuracy']
    )

epoch_historyLSTM = LSTM_Model.fit(x_train, y_train, 
                              epochs =200, 
                              validation_data=(x_test, y_test) 
                              )

plt.plot(epoch_historyLSTM.history['accuracy'], label='Accuracy')
plt.plot(epoch_historyLSTM.history['val_accuracy'])
plt.title("Accuracy of the LSTM Model")
plt.show()

y_pred = LSTM_Model.predict(x_test)
y_pred = y_pred.argmax(axis=1)
y_test_labels = y_test.argmax(axis=1)
cnf_matrix_auth = confusion_matrix(y_test_labels, y_pred)
# print(classification_report(y_test_labels, y_pred))
#make a nicer figure for the confusion matrix
make_confusion_matrix(cnf_matrix_auth)


