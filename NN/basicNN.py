import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow.keras as keras

dataset = np.loadtxt('processedData.csv', delimiter=',')
print(dataset.shape)
x = dataset[:,0:25]
y = dataset[:,25:50]

model = Sequential()
model.add(Dense(40, input_shape=(25,), activation='relu'))
model.add(Dense(80, activation='relu'))
model.add(Dense(160, activation='relu'))
model.add(Dense(80, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(25, activation='relu'))

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.fit(x, y, epochs=150, batch_size=10)

_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))