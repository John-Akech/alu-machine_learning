import tensorflow as tf

def flip_image(image):
    """
    Flips an image horizontally.

    Args:
        image (tf.Tensor): A 3D tensor of shape [height, width, channels] 
                           representing the image to flip.

    Returns:
        tf.Tensor: The flipped image.
    """
    # Ensure the input is a 3D tensor
    if len(image.shape) != 3:
        raise ValueError("Input image must be a 3D tensor with shape [height, width, channels].")
    
    # Flip the image horizontally
    flipped_image = tf.image.flip_left_right(image)
    
    return flipped_image
