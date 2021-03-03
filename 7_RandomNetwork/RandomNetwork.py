import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def main():
    # initialise random network
    rand_net = RandomNet(non_lin="tanh")

    # examine network weights
    rand_net.print_weights()
    
    # define some arbitrary input data, say a straight line along the x and another along the y axis
    n = 10
    x_axis = np.column_stack((np.arange(n),np.zeros(n))) 
    y_axis = np.column_stack((np.zeros(n),np.arange(n))) 
    input = np.concatenate((x_axis,y_axis),axis=0)
    plot_2D(input)

    for image in rand_net.transform(input):
        plot_2D(image)


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