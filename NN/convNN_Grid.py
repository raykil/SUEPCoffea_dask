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

# Define the create_model function to create the Keras model
def create_model(filters=128, kernel_size=(3,3), dropout_rate=0.2, dense_nodes = [1024, 712, 400]):
    model = Sequential()
    model.add(Conv2D(filters=filters, kernel_size=kernel_size, input_shape=(20, 20, 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=2))
    model.add(Dropout(dropout_rate))
    model.add(layers.Flatten())
    model.add(Dense(dense_nodes[0], activation='relu'))
    model.add(Dropout(dropout_rate))
    model.add(Dense(dense_nodes[1], activation='relu'))
    model.add(Dropout(dropout_rate))
    model.add(Dense(dense_nodes[2], activation='sigmoid'))
    model.add(layers.Reshape(target_shape=(20, 20, 1)))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Load the dataset
dataset = np.loadtxt('processedData_Private_20x20.csv', delimiter=',')
x = dataset[:, 0:400]
y = dataset[:, 400:800]
x_3D = np.reshape(x, (x.shape[0], 20, 20, 1))
y_3D = np.reshape(y, (y.shape[0], 20, 20, 1))
X_train, X_test, y_train, y_test = sk.train_test_split(x_3D, y_3D, test_size=0.2)

# Split training data into training and validation sets
X_train, X_val, y_train, y_val = sk.train_test_split(X_train, y_train, test_size=0.2)

# Create a KerasRegressor based on the create_model function
model = KerasRegressor(build_fn=create_model)

# Define the grid search parameters
param_grid = {
    'filters': [128, 256],
    #'kernel_size': [3, 5, 7],
    #'dropout_rate': [0.1, 0.2],
    'dense_nodes': [[1024, 712, 400], [2048, 1024, 400]],
    'batch_size': [int(.01*X_train.shape[0])],
    'epochs': [100, 150, 200]
}

print(int(.001*X_train.shape[0]))
print(int(.01*X_train.shape[0]))

# Create the GridSearchCV instance
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=2)

# Define early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=25, restore_best_weights=True)

# Perform the grid search with early stopping
grid_result = grid_search.fit(X_train, y_train, callbacks=[early_stopping], validation_data=(X_val, y_val))


# Print the best parameters and score
print("Best Parameters: ", grid_result.best_params_)
print("Best Score: ", grid_result.best_score_)

# Access the grid search results
cv_results = grid_result.cv_results_
params = cv_results['params']
mean_test_scores = cv_results['mean_test_score']

# Extract the hyperparameters
filters = [param['filters'] for param in params]
#kernel_sizes = [param['kernel_size'] for param in params]
#dropout_rates = [param['dropout_rate'] for param in params]
#batch_sizes = [param['batch_size'] for param in params]
epochs = [param['epochs'] for param in params]

'''
# Create a scatter plot of the mean test scores
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(filters, dropout_rates, mean_test_scores, cmap='viridis')
ax.view_init(30, 45)
ax.set_xlabel('Filters')
ax.set_ylabel('Dropout Rate')
ax.set_zlabel('Mean Test Score')
ax.set_title('Grid Search Results')
plt.savefig('GS_filt_drop_2D.png')

plt.clf()


fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(batch_sizes, epochs, mean_test_scores, cmap='viridis')
ax.view_init(30, 45)
ax.set_xlabel('Batch Sizes')
ax.set_ylabel('Epochs')
ax.set_zlabel('Mean Test Score')
ax.set_title('Grid Search Results')
plt.savefig('GS_BS_Epochs_2D.png')

plt.clf()
'''

# Get the best model from the grid search
best_model = grid_result.best_estimator_.model

# Evaluate the best model on the test dataset
test_loss, test_accuracy = best_model.evaluate(X_test, y_test)

print("Test Loss: ", test_loss)
print("Test Accuracy: ", test_accuracy)

# Train the best model and capture the history
history = best_model.fit(X_train, y_train, batch_size = int(.01*X_train.shape[0]), epochs = grid_result.best_params_['epochs'], validation_data=(X_val, y_val), callbacks=[early_stopping])

# Plotting test loss and accuracy
plt.figure(figsize=(12, 6))

xvals = range(1, len(history.history['val_loss']) + 1)

# Plot test loss
plt.subplot(1, 2, 1)
plt.plot(xvals, history.history['val_loss'])
plt.title('Test Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')

# Plot test accuracy
plt.subplot(1, 2, 2)
plt.plot(xvals, history.history['val_accuracy'])
plt.title('Test Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

plt.tight_layout()
plt.savefig('BestModel_TestResults_Epoch_BatchSize_2D.png')