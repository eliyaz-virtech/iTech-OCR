#Import libraries 
import tensorflow as tf
import matplotlib.pyplot as plt

#Load dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

#Data preparation 
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

#Model creation
model = tf.keras.models.Sequential()

#Add input layer
model.add(tf.keras.layers.Flatten())

#Add hidden layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))

#Add output layer
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

#Compile model 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Train model with the given inputs 
model.fit(x_train, y_train, epochs=3)

#Evaluating already trained model using the test data. Return the loss value and metrics values for the model.
val_loss, val_acc = model.evaluate(x_test, y_test)

