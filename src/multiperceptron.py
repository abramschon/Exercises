# Implementing a multi-class perceptron to separate simulated data

from perceptron import create_data, accuracy
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Create data
    shape=(100,2)
    X,Y = create_data(shape) # we will redefine the labels in a second
    # define a perceptron using "model" weight vectors
    ideal_perc = MultiClassPercepton(shape[1],4,np.array([[ 1, 1,-1,-1],
                                                          [ 1,-1,-1, 1]]))
    Y = ideal_perc.predict(X)
    plot_2D_data(X,Y)

    # Create Perceptron with randomised weights
    percy = Percepton(shape[1], 4)

    Y_pred = percy.predict(X) #initial predictions
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
    def __init__(self, features, classes, W=None):
        """
        A perceptron that outputs the label of the class of each observation
        
        args:
            features: int - how many features each observation has, 
                used to initialise weights
            classes: int - how many classes the data has
            W: np array with dimensions (features, classes)
        """
        if W is None:
            self.W = np.random.normal(size=(features, classes))
        else:
            self.W = W

    def predict(self, X):
        """
        Takes the dot product of each observation with each weight vector and returns the label of the weight vector associate with the largest product
        """
        products = X @ self.W
        Y_pred = np.argmax(products, axis=1) 
        return Y_pred

    #TO DO
    def update(self, x, y):
        """
        Updates the weights based to better classify misclassified prediction
        Expects a column vector for observation x
        """
        self.W = self.W + y*x


# TO DO modify this to plot multiple weight vectors
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