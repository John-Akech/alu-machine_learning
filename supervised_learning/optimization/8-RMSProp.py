#!/usr/bin/env python3
""" Training with RMSProp optimizer
"""

import tensorflow as tf

def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """Creates the training operation for a neural network using the RMSProp optimization algorithm.
    
    Args:
        loss: Loss function of the network.
        alpha: Learning rate.
        beta2: RMSProp decay rate.
        epsilon: Small value to avoid division by zero.
        
    Returns:
        The RMSProp optimization operation.
    """
    # Use the updated TensorFlow API
    optimizer = tf.optimizers.RMSprop(learning_rate=alpha, rho=beta2, epsilon=epsilon)
    
    # Minimize the loss function
    train_op = optimizer.minimize(loss)
    return train_op
