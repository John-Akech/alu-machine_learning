import tensorflow as tf

def rotate_image(image):
    """
    Rotates an image by 90 degrees counter-clockwise.

    Args:
        image (tf.Tensor): A 3D tensor of shape [height, width, channels] 
                           representing the image to rotate.

    Returns:
        tf.Tensor: The rotated image.
    """
    # Ensure the input is a 3D tensor
    if len(image.shape) != 3:
        raise ValueError("Input image must be a 3D tensor with shape [height, width, channels].")
    
    # Rotate the image by 90 degrees counter-clockwise
    rotated_image = tf.image.rot90(image, k=1)
    
    return rotated_image
