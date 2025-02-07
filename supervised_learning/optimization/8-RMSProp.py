#!/usr/bin/env python3
""" Training with RMSProp
"""

import tensorflow as tf

def create_RMSProp_op(loss, alpha, beta2, epsilon, momentum=0.0):
    """ Creates the training operation for a neural network in TensorFlow
        using the RMSProp optimization algorithm.

        Args:
            loss: The loss of the network.
            alpha: The learning rate.
            beta2: The decay rate for the moving average of the squared gradient.
            epsilon: A small constant for numerical stability.
            momentum: (Optional) Momentum parameter. Default is 0.0.

        Returns:
            The RMSProp optimization operation.
    """
    optimizer = tf.optimizers.RMSprop(learning_rate=alpha, rho=beta2, epsilon=epsilon, momentum=momentum)
    return optimizer.minimize(loss)
