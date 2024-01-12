import numpy as np

class Neuron:
    '''Class describing a single neuron'''

    def __init__(self, input_size, activation_function, rng):
        self.weights = rng.multivariate_normal(np.zeros(input_size),
                                               np.diag([.1 for i in range(input_size)]),
                                               )
        self.weights = self._init_weights(size, weight_initialization)
        self.activation_function = self._select_activation_function(activation_function)
    
    def _init_weights(self, size, weight_initialization):
        pass

    def _select_activation_function(self, activ=ation_function):
        pass

    def combine_input(self, input):
        self.combination = np.sum(np.dot(input, self.weights))

    def output(self):
        return self.activation_function(self.combination)
