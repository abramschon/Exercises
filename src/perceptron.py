# Implementing a multi-class perceptron to separate simulated data

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create data
    shape=(5,2)
    X,Y = create_data(shape)
    plot_2D_data(X,Y)

    # Create Perceptron
    percy = Percepton(shape[1])
    print(percy.W)

    predictions = percy.predict(X)
    print(predictions)

    # Update weights

class Percepton:
    def __init__(self, features):
        """
        A perceptron that outputs a binary classification -1 or 1
        
        args:
            features: int - how many features each observation has, 
                used to initialise weights
        """
        self.W = np.random.normal(size=(features,1))

    def predict(self, X):
        """
        Assumes X has rows for observations and cols for features
        """
        Y_pred = np.sign(X @ self.W)

        return Y_pred

    def update(self, x, y, y_pred):
        """
        Updates the weights based on whether prediction is correct
        Expects a column vector for observation x
        """
        adjust = [-1,1][y==y_pred]
        self.W = self.W + adjust*x



def create_data(shape=(50,2), resp_func=lambda X: np.sign(np.sum(X, axis=1, keepdims=True))):
    """
    Creates data with shape (rows, cols), 
        rows corresponding to the number of observations,
        cols corresponding to the features of each observation
    Then for each observations label, it applies the given function, which by default
    returns the sign of the sum of the features.
    """
    X = np.random.uniform(-1,1,size=shape)
    Y = resp_func(X)
    return X,Y

def plot_2D_data(X,Y):
    """
    For 2D data, plot the data indicating which class it falls into
    """
    plt.scatter(X[:,0], X[:,1], c=Y.flatten(), cmap=plt.cm.Set1)
    print(Y.astype(int).flatten)
    plt.show()



if __name__ == "__main__":
    main()