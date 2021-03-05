import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def main():
    # initialise random network
    rand_net = RandomNet(
        w_sd=0.2, #weight standard deviation
        b_sd=0, #bias standard deviation
        shapes=[2,500,500,500,500,500,2], #no. units in each layer
        non_lin="sigmoid" #type of non-linearity applied to each layer         
    )

    # examine network weights
    rand_net.print_weights()
    
    # define some arbitrary input data, a grid
    m = 10
    n = 10
    input = np.array([[0,0]])
    for i in range(m):
        vert = np.column_stack((i*np.ones(n),np.arange(n))) #create vertical lines at different heights
        input = np.concatenate((input,vert),axis=0)
    
    # visualise how each layer transforms data
    plot_2D(input)
    outputs = rand_net.transform(input)

    plot_2D(outputs[-1])
    

    


def plot_2D(data):
    """
        Expects a Nx2 array of data, which is plots in a 2D plane
    """
    lower = np.min(data)
    upper = np.max(data)
    plt.scatter(data[:,0],data[:,1])
    plt.xlim([lower, upper]) 
    plt.ylim([lower, upper]) 
    plt.show()

class RandomNet:
    def __init__(self,
                 w_sd=1, #weight standard deviation
                 b_sd=1, #bias standard deviation
                 shapes=[2,2,2], #layers and units per layer including input shape  e.g. [2,2,2] - 2 inputs, then 2 layers of 2 units each
                 non_lin="sigmoid" #type of non-linearity applied to each layer
                 ):    
        self.w_sd = w_sd
        self.b_sd = b_sd
        
        #initialise random network 
        self.network = tf.keras.Sequential()
        self.network.add( tf.keras.Input( shape=(shapes[0],) ) )
        for shape in shapes[1:]:
            self.network.add(
                tf.keras.layers.Dense(
                    units=shape,
                    activation=non_lin,
                    kernel_initializer= tf.keras.initializers.RandomNormal(stddev=w_sd),
                    bias_initializer= tf.keras.initializers.RandomNormal(stddev=b_sd)
                )
            )

    def print_weights(self):
        for layer in self.network.layers:
            print("Weights")
            print(layer.kernel.numpy())
            print("Bias")
            print(layer.bias.numpy())

    def transform(self, input):
        """
            Takes in input data and returns image of data after each layer 
        """
        outputs = []
        for layer in self.network.layers:
            input = layer(input).numpy() #pass input through layer
            outputs.append(input)
            
        return outputs
                
if __name__=="__main__":
    main()