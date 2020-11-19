# Implementing a perceptron to separate simulated data

import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create data
    shape=(50,2)
    X,Y = create_data(shape)

    # Create Perceptron
    percy = Percepton(shape[1])

    Y_pred = percy.predict(X) #initial predictions
    plot_2D_data(X,Y,percy.W)

    # Update weights until accuracy is 1.
    for i in range(10): #arbitrary number of iterations
        acc = accuracy(Y, Y_pred)
        print(f"Accuracy: {acc}")
        if acc == 1:
            break
        #pick first missed predictions and update
        miss = np.where(Y!=Y_pred)[0][0]
        x = X[miss,:]
        y = Y[miss,:]
        print(miss, x.shape, y.shape)
        percy.update(x[:,None], y)
        
        plot_2D_data(X,Y,percy.W) # show result of updating vector

        Y_pred = percy.predict(X) # make new predictions


    

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

    def update(self, x, y):
        """
        Updates the weights based to better classify misclassified prediction
        Expects a column vector for observation x
        """
        self.W = self.W + y*x

def accuracy(Y, Y_pred):
    """
    Returns number of correctly classified observations divided by total no. observations 
    """
    return np.sum(Y==Y_pred) / Y.shape[0]

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

def plot_2D_data(X,Y, W=None):
    """
    For 2D data, plot the data indicating which class it falls into
    """
    plt.xlim((-1,1))
    plt.ylim((-1,1))
    plt.scatter(X[:,0], X[:,1], c=Y.flatten(), cmap=plt.cm.Set1)
    if W is not None:
        norm_W = W.flatten()/np.linalg.norm(W)
        plt.plot( [0,norm_W[0]],[0,norm_W[1]], "-") #plot normalise
    plt.show()



if __name__ == "__main__":
    main()