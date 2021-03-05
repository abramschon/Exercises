# Variation and Signal Propagation in Random Networks

Based on a paper by [Poole et al](https://arxiv.org/pdf/1606.05340.pdf), I want to visualize how 2D shapes are transformed as they move through random neural networks initialized with different amounts of variation on the weights and biases. 

I want to code up a deep neural network defined by:
- Variance of the weights
- Variance of the biases 
- Number of layers
- Number of units per layer (though I want to stick to 1-3 units for the sake of visualization)
- Type of non-linearity used


I want to be able to look at the outputs of each layer (peer into 'hidden space'), so I need some function that extracts the activations out of each layer and plots it. 

Perhaps later, also consider some simple toy supervised learning problems, and visualizing the decision plane at each layer of the network.