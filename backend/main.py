# Symptom match code
# Predict disease using symptoms 
# 1) Decision Tree or Random Forest
# 2) Neural Networks with softmax output layer -- for a rank of diseases depending on probability of disease match

# import libraries
from xml.etree.ElementPath import prepare_descendant
import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense

from config import *


def DecisionTree(X_train, y_train, X_test, y_test):
    # 96% accuracy

    #train and fit model
    model = tree.DecisionTreeClassifier()
    model.fit(X_train, y_train)

    #test model on test set
    predictions = model.predict(X_test)

    wrong = 0
    total = len(y_test)
    for i in range(total):
        if predictions[i]!=y_test[i]:
            wrong+=1
            # print(predictions[i]," -- ", y_test[i])
    
    print("Accuracy Decision Tree: {}/{} are corrrect -- {}%".format(total-wrong, total, (total-wrong)/total*100))
    return


def RandomForest(X_train, y_train, X_test, y_test):
    # 100% accuracy    

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    wrong = 0
    total = len(y_test)
    for i in range(total):
        if predictions[i]!=y_test[i]:
            wrong+=1
            # print(predictions[i]," -- ", y_test[i])
    
    print("Accuracy RandomForest: {}/{} are corrrect -- {}%".format(total-wrong, total, (total-wrong)/total*100))
    return

def NeuralNet(X_train, y_train, X_test, y_test, n=5):

    X_train=tf.strings.to_number(X_train, out_type=tf.dtypes.int64)
    X_test=tf.strings.to_number(X_test, out_type=tf.dtypes.int64)

    #convert y_train to numerical
    y_train_num = []
    for dis in y_train:
        #TODO: make dis case insensitive
        dis = dis.strip()
        y_train_num.append(np.where(diseases==dis))
    y_train_num = np.array(y_train_num)
    # print(y_train_num)

    for i in range(len(y_train)):    
        assert y_train[i].strip()==diseases[y_train_num[i]][0][0].strip()
        # print(y_train[i], y_train_num[i], diseases[y_train_num[i]])

    model = Sequential(
    [ 
        Dense(400, activation = 'relu'),
        Dense(25, activation = 'relu'),
        Dense(120, activation = 'relu'),
        Dense(15, activation = 'relu'),
        Dense(len(diseases), activation = 'linear')    # < softmax activation here
    ]
    )

    model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        # loss=tf.keras.losses.SparseCategoricalCrossentropy(),
        optimizer=tf.keras.optimizers.Adam(0.001),
    )

    model.fit(
        X_train,y_train_num,
        epochs=10
    )

    predictions = model.predict(X_test)

    #convert to probabilities (of each disease)
    prob_disease = tf.nn.softmax(predictions).numpy()
    prediction_names = []

    #convert probabilities to categorical values == disease names
    #by choosing highest prob index as predicted disease

    for prob in prob_disease:
        i = prob.argsort()[-n:][::-1]
        i = np.array(i)
        prediction_names.append(diseases[i])

    
    wrong = 0
    total = len(y_test)
    for i in range(total):
        if prediction_names[i][0]!=y_test[i]:
            wrong+=1
            # print(predictions[i]," -- ", y_test[i])
    
    acc_str = "Accuracy Nueral Network: {}/{} are corrrect -- {}%".format(total-wrong, total, (total-wrong)/total*100)
    print(acc_str)

    print(prediction_names[0])
    return prediction_names[0]

# load data
def load_data():
    # list of features == symptoms in this case

    data = csv_to_data()
    X , y = [x[:-1] for x in data], [x[-1] for x in data]
    X = np.asarray(X)
    y = np.asarray(y)
    
    return X, y

def csv_to_data():
    train = []
    
    with open("symptom_to_type.csv", mode="r") as file:

        #read csv file
        csvfile = csv.reader(file)
        next(csvfile)
        for lines in csvfile:
            train.append([int(x) for x in lines[:-1]]+[lines[-1]])
    
    train = np.asarray(train)
    return train


def main():
    
    # print(load_data())

    X, y = load_data()
    # split data into train, test and validation sets
    X_train, X_rem, y_train, y_rem = train_test_split(X, y, test_size=0.8)
    X_test, X_val, y_test, y_val = train_test_split(X_rem, y_rem, test_size=0.5)

    # DecisionTree(X_train, y_train, X_rem, y_rem)
    # RandomForest(X_train, y_train, X_rem, y_rem)
    pred = NeuralNet(X_train, y_train, X_rem, y_rem)
    return np.ndarray.tolist(pred)

if __name__ == "__main__":
    main()


# split data into train, test, and validation sets
# train data
    # decision tree
    # random forest
    # neural networks   

# test models / inference