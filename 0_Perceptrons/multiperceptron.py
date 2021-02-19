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
    Y = ideal_perc.predict(X) #use this to label simulated data

    # Create Perceptron with randomised weights
    percy = MultiClassPercepton(shape[1], 4)

    Y_pred = percy.predict(X) #initial predictions
    plot_2D_data(X,Y,percy.W)

    # Update weights until accuracy is 1.
    for i in range(50): #arbitrary number of iterations
        acc = accuracy(Y, Y_pred)
        print(f"Iteration: {i}, Accuracy: {acc}")
        if acc == 1:
            break
        #pick first missed predictions and update
        miss = np.where(Y!=Y_pred)[0][0] #np.where returns a tuple
        x = X[miss,:]
        y = Y[miss]
        y_pred = Y_pred[miss]

        # update weights and plot updated vectors
        percy.update(x, y, y_pred)
        
        plot_2D_data(X,Y,percy.W) # show result of updating vector

        Y_pred = percy.predict(X) # make new predictions


    

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
    def update(self, x, y, y_pred):
        """
        Updates the weights based to better classify misclassified prediction
        """
        self.W[:,y] += x #make the vector that should "represent" x more in the direction of x
        self.W[:,y_pred] -= x #make the vector that incorrectly "represented x" less in that direction 


def plot_2D_data(X,Y, W=None):
    """
    For 2D data, plot the data indicating which class it falls into
    """
    plt.xlim((-1,1))
    plt.ylim((-1,1))
    plt.scatter(X[:,0], X[:,1], c=Y.flatten(), cmap=plt.cm.Set1)
    if W is not None:
        for vec in W.T:
            norm_vec = vec.flatten()/np.linalg.norm(vec)
            plt.plot( [0,norm_vec[0]],[0,norm_vec[1]], "-") #plot normalised vector
    plt.show()



if __name__ == "__main__":
    main()
