import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, Flatten, Dropout, MaxPooling1D, MaxPooling2D, Conv2D
from tensorflow.keras import layers
import tensorflow.keras as keras
import sklearn.model_selection as sk
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping

dataset = np.loadtxt('processedData_Private_20x20.csv', delimiter=',')
print(dataset.shape)
x = dataset[:,0:400]
y = dataset[:,400:800]
x_3D = np.reshape(x, (x.shape[0], 20, 20, 1))
y_3D = np.reshape(y, (y.shape[0], 20, 20, 1))

X_train, X_test, y_train, y_test = sk.train_test_split(x_3D, y_3D, test_size=0.2)

model = Sequential()
model.add(Conv2D(filters=128, kernel_size=(3, 3), input_shape=(20, 20, 1), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.2))
model.add(layers.Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(712, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(400, activation='sigmoid'))
model.add(layers.Reshape(target_shape=(20, 20, 1)))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

early_stopping = EarlyStopping(monitor='val_loss', patience=25, restore_best_weights=True)

history = model.fit(X_train, y_train, callbacks=[early_stopping], validation_split = .2, epochs=100, batch_size=int(.01*X_train.shape[0]))

plt.plot(history.history['val_loss'], label = 'val_loss')
plt.plot(history.history['loss'], label = 'loss')
plt.title('Model Training Metrics')
plt.yscale('log')
plt.ylabel('Value')
plt.xlabel('Epoch')
plt.legend(fontsize = "6", loc='upper right')
plt.savefig('TrainingMetrics_loss.png')

plt.clf()

plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.plot(history.history['accuracy'], label = 'accuracy')
plt.title('Model Training Metrics')
plt.yscale('log')
plt.ylabel('Value')
plt.xlabel('Epoch')
plt.legend(fontsize = "6", loc='upper right')
plt.savefig('TrainingMetrics_acc.png')

plt.clf()

print('Test Results!')

model.evaluate(X_test, y_test)