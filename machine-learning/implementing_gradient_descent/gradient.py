import numpy as np
from data_prep import features, targets, features_test, targets_test

# Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of activation function.
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

np.random.seed(42)

n_records, n_features = features.shape
last_loss = None

weights = np.random.normal(scale= 1 / n_features**.5, size = n_features)

# Hyper parameters
epochs = 1000
learnrate = 0.5

p = 0

for e in range(epochs):
    delta_weight = np.zeros(features.shape[1])
    for x, y in zip(features.values, targets):

        output = sigmoid(np.dot(x, weights))
        error = y - output

        delta_weight += error * output * (1 - output) * x

    weights += learnrate * delta_weight/n_records

    if e % (epochs/10) == 0:
        out = sigmoid(np.dot(features, weights))

        loss = np.mean((out - targets) ** 2)

        if last_loss and last_loss < loss:
            print("Train loss: ", loss, " WARNING - loss increasing")
        else:
            print("Train loss: ", loss)
        last_loss == loss

test_out = sigmoid(np.dot(features_test, weights))
predictions = test_out > 0.5

accuracy = np.mean(predictions == targets_test)
print("Prediction accuracy: {:.3f}".format(accuracy))