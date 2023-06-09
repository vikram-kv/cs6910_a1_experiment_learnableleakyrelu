import numpy as np

# new activation functions to be added following the template seen here.

# sigmoid activation function and derivative
def sigmoid_value(x):
    return 1.0/(1.0 + np.exp(-x))

def sigmoid_deriv(fx):
    return (1.0 - fx) * fx

# relu activation function and derivative
def relu_value(x):
    return np.where(x>0, x, 0.0)
    
def relu_deriv(fx):
    return np.where(fx>0, 1.0, 0.0)

# tanh activation function and derivative
def tanh_value(x):
    y, z = np.exp(x), np.exp(-x)
    return (y-z)/(y+z)

def tanh_deriv(fx):
    return (1.0 - fx) * (1.0 + fx)

# linear activation function and derivative
def linear_value(x):
    return x

def linear_deriv(fx):
    return np.ones_like(fx)

# leaky_relu activation function and derivative
def leakyrelu_value(x, alpha):
    next = np.maximum(x, (x.T * alpha).T)
    return next

def leakyrelu_deriv(fx, alpha):
    next = ((np.ones_like(fx)).T * alpha).T
    return np.where(fx>0,1,next)

# elu activation function and derivative
def elu_value(x):
    return np.where(x>0, x, 1.0 * (np.exp(x) - 1))
    
def elu_deriv(fx):
    return np.where(fx>0, 1.0, fx + 1.0)

# function to return the function operator and derivative operator for a activation function by name
def get_act_func_and_deriv(name : str):
    if (name == 'linear'):
        return linear_value, linear_deriv
    elif (name == 'tanh'):
        return tanh_value, tanh_deriv
    elif (name == 'sigmoid'):
        return sigmoid_value, sigmoid_deriv
    elif (name == 'relu'):
        return relu_value, relu_deriv
    elif (name == 'leakyrelu'):
        return leakyrelu_value, leakyrelu_deriv
    elif (name == 'elu'):
        return elu_value, elu_deriv
    else:
        raise Exception('Activation Function Not Implemented'); exit(-1)