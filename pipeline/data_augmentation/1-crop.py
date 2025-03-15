import tensorflow as tf

def crop_image(image, size):
    """
    Performs a random crop of an image.

    Args:
        image (tf.Tensor): A 3D tensor of shape [height, width, channels] 
                           representing the image to crop.
        size (tuple): A tuple (crop_height, crop_width) specifying the size 
                      of the crop.

    Returns:
        tf.Tensor: The cropped image.
    """
    # Ensure the input is a 3D tensor
    if len(image.shape) != 3:
        raise ValueError("Input image must be a 3D tensor with shape [height, width, channels].")
    
    # Validate the size parameter
    if len(size) != 2 or size[0] <= 0 or size[1] <= 0:
        raise ValueError("Size must be a tuple of two positive integers (crop_height, crop_width).")
    
    # Perform the random crop
    crop_height, crop_width = size
    cropped_image = tf.image.random_crop(image, size=[crop_height, crop_width, image.shape[-1]])
    
    return cropped_image
