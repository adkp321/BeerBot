#Linear Regression with Python and Tensorflow
#!pip install -q sklearn

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf



# Load dataset. df is dataframe

dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
#pop out a column
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck', 'embark_town', 'alone']
NUMERICAL_COLUMNS = ['age', 'fare']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique() #gets a list of all unique values from given feature column
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERICAL_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)


# Create an input function
"""This is about to be a complex section of code.
    To Keep it as simple as possible I have added additional notes.
    Please read all of the notes
    Input Function
    This should be recycled"""
def make_input_fn(data_df, label_df, num_epochs=1000, shuffle=True, batch_size=32): #def is used to create a function in python. Epochs are the number of times the whole dataset is ran through. Batch size is the amount of data in each run.
  def input_funtion(): #inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df)) #create tf.data.Dataset object with data and its
    if shuffle:
      ds = ds.shuffle(1000) #randomizes the order of the data
    ds = ds.batch(batch_size).repeat(num_epochs) # splits up the data into the batch sizes and repeats the number of epochs specified 
    return ds #return a batch of the dataset
  return input_funtion # return a function object for use

train_input_fn = make_input_fn(dftrain, y_train)# here we call the input_function that was returned
eval_input_fn= make_input_fn(dfeval,y_eval, num_epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns) #Use the LinearClassifier in the estimator from Tensorflow

linear_est.train(train_input_fn) #train
result = linear_est.evaluate(eval_input_fn) #get model metrics/stats by testing data

clear_output() #clears console output. The only reason we needed to import IPython
print(result['accuracy'])#the result variable is simply a dict of stats about our model
print(result)

"""Getting actual predictions"""
result = list(linear_est.predict(eval_input_fn))
print(dfeval.loc[0])
print(result[0]['probabilities'][1]) #probability of surviving the titanic
