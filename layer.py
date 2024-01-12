import numpy as np

from .library import activation

class DenseLayer:
    '''Neural Network layer'''

    def __init__(self, input_size: int, rng: np.random.Generator, activation_func: str):
        self.weights = rng.multivariate_normal(mean=np.zeros(input_size),
                                               cov = np.diag([.05 for _ in range(input_size)]),
                                               size = (input_size, input_size, 3))
        self.activation_func = self._select_activation_func(activation_func)

    def _select_activation_func(self, activation_func: str):
        clean_func = activation_func.lower()
        match clean_func:
            case 'sigmoid':
                return activation.sigmoid
            case 'relu':
                return activation.relu
            case 'leaky_relu':
                return activation.leakyRelu

    def forward(self, input):
        '''Conduct the forward pass of the layer. Takes input and multiplies by
        the weights to obtain the output layer.
        '''
        pass

    def backward_prop(self):
        pass


if __name__=='__main__':
    rng = np.random.default_rng(42)
    layer = DenseLayer(32, rng, 'leaky_relu')
    print(layer.weights)
    print(layer.activation_func)
    print(layer.activation_func(17))
    print(layer.activation_func(-77))


