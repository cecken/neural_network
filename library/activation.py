import numpy as np

def sigmoid(input: float):
    '''Returns sigmoid activation function of input''' 
    return 1 / (1 + np.exp(-input))

def relu(input: float):
    ''' Returns relu activation of input'''
    return max(0, input)

def leakyRelu(input: float):
    if input > 0:
        return input
    return input / 1000
    
