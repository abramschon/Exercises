# Implementing a multi-class perceptron to separate simulated data

from perceptron import create_data
import numpy as np
import matplotlib.pyplot as plt

def main():
    # # Create data
    # shape=(50,2)
    # X,Y = create_data(shape)

    # # Create Perceptron
    # percy = Percepton(shape[1])

    # Y_pred = percy.predict(X) #initial predictions
    # plot_2D_data(X,Y,percy.W)

    # # Update weights until accuracy is 1.
    # for i in range(10): #arbitrary number of iterations
    #     acc = accuracy(Y, Y_pred)
    #     print(f"Accuracy: {acc}")
    #     if acc == 1:
    #         break
    #     #pick first missed predictions and update
    #     miss = np.where(Y!=Y_pred)[0][0]
    #     x = X[miss,:]
    #     y = Y[miss,:]
    #     print(miss, x.shape, y.shape)
    #     percy.update(x[:,None], y)
        
    #     plot_2D_data(X,Y,percy.W) # show result of updating vector

    #     Y_pred = percy.predict(X) # make new predictions


    

class MultiClassPercepton:
    def __init__(self, features, classes):
        """
        A perceptron that outputs the label of the class of each observation
        
        args:
            features: int - how many features each observation has, 
                used to initialise weights
            classes: int - how many classes the data has
        """
        self.W = np.random.normal(size=(features, classes))

    def predict(self, X):
        """
        Assumes X has rows for observations and cols for features
        """
        products = np.sign(X @ self.W)
        Y_pred = np.argmax(products, axis=0) #check axis 0 works

        return Y_pred

    # adjust so that we subtract feature from incorrect vector and add feature to correct vector
    def update(self, x, y):
        """
        Updates the weights based to better classify misclassified prediction
        Expects a column vector for observation x
        """
        self.W = self.W + y*x

#check this works
def accuracy(Y, Y_pred):
    """
    Returns number of correctly classified observations divided by total no. observations 
    """
    return np.sum(Y==Y_pred) / Y.shape[0]


# modify this to plot multiple weight vectors
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