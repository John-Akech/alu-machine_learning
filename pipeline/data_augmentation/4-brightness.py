import tensorflow as tf

def change_brightness(image, max_delta):
    """
    Randomly changes the brightness of an image.

    Args:
        image (tf.Tensor): A 3D tensor of shape [height, width, channels] 
                           representing the image to alter.
        max_delta (float): The maximum amount the image should be brightened 
                           or darkened. Must be non-negative.

    Returns:
        tf.Tensor: The altered image with adjusted brightness.
    """
    # Ensure the input is a 3D tensor
    if len(image.shape) != 3:
        raise ValueError("Input image must be a 3D tensor with shape [height, width, channels].")
    
    # Validate the max_delta parameter
    if not isinstance(max_delta, (int, float)) or max_delta < 0:
        raise ValueError("max_delta must be a non-negative number.")
    
    # Randomly adjust the brightness
    altered_image = tf.image.random_brightness(image, max_delta=max_delta)
    
    return altered_image
