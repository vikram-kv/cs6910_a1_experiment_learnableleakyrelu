# cs6910_a1_experiment_learn_relu

Addendum to cs6910 assignment 1. Here, the alpha (negative region co-efficient) has been made learnable. Other than that, the usage instruction remains the same.

To use the learnable leaky-relu, run 

$ python3 train.py 

to train and test the network for the default values for the hyperparameters (here, default activation function is relu).

Other values for the remaining hyperparameters may be given using the argparse help available from 

$ python3 train.py -h

We calculate the alpha (negative region co-efficient in leaky relu) gradients using the technique Prof. Mitesh used for maxout neuron. The gradient is calculated for every neuron in the current layer and an indicator function is used to mask out only those neurons in the negative activation region for that should be updated during backprop.
