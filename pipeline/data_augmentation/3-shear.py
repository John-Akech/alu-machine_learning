import tensorflow as tf

def shear_image(image, intensity):
    """
    Randomly shears an image.

    Args:
        image (tf.Tensor): A 3D tensor of shape [height, width, channels] 
                           representing the image to shear.
        intensity (float): The intensity with which the image should be sheared.

    Returns:
        tf.Tensor: The sheared image.
    """
    # Ensure the input is a 3D tensor
    if len(image.shape) != 3:
        raise ValueError("Input image must be a 3D tensor with shape [height, width, channels].")
    
    # Validate the intensity parameter
    if not isinstance(intensity, (int, float)) or intensity <= 0:
        raise ValueError("Intensity must be a positive number.")
    
    # Randomly shear the image
    sheared_image = tf.keras.preprocessing.image.random_shear(
        image.numpy(),  # Convert tf.Tensor to numpy array
        intensity=intensity,
        channel_axis=-1  # Channels are the last axis
    )
    
    # Convert the result back to a tf.Tensor
    return tf.convert_to_tensor(sheared_image)
