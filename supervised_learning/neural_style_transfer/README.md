# Neural Style Transfer Project

## Overview

This project implements **Neural Style Transfer (NST)** using TensorFlow, enabling the fusion of the content of one image with the style of another to produce a new, stylized image. The technique leverages convolutional neural networks (CNNs) to extract and recombine content and style features from images.

## Learning Objectives

By the end of this project, you should be able to:

- **Understand Neural Style Transfer**: Grasp the concept of blending content and style from two images using deep learning techniques.
- **Define and Compute a Gram Matrix**: Learn how to calculate the Gram matrix, which captures style information by measuring feature correlations.
- **Calculate Style Cost**: Understand how to quantify the difference in style between images using the Gram matrix.
- **Calculate Content Cost**: Learn how to measure the difference in content between images based on feature representations.
- **Utilize TensorFlow's Eager Execution**: Gain proficiency in TensorFlow's imperative programming environment that evaluates operations immediately.
- **Implement Gradient Tape**: Use TensorFlow's `GradientTape` to record operations for automatic differentiation.
- **Perform Neural Style Transfer**: Combine the above concepts to execute NST and generate stylized images.

## Project Structure

- `models/`: Contains pre-trained models used for feature extraction.
- `images/`: Includes sample content and style images.
- `output/`: Stores the generated stylized images.
- `notebooks/`: Jupyter notebooks demonstrating the NST process step-by-step.
- `scripts/`: Python scripts for training and applying style transfer models.
- `requirements.txt`: Lists the Python dependencies required to run the project.
- `README.md`: This file, providing an overview and instructions for the project.

## Requirements

- **General**:
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 16.04 LTS using Python 3.5
  - Files will be executed with `numpy` version 1.15 and `tensorflow` version 1.12
  - All files should end with a new line
  - The first line of all Python files should be exactly `#!/usr/bin/env python3`
  - A `README.md` file at the root of the project is mandatory
  - Code should adhere to the `pycodestyle` style (version 2.4)
  - All modules, classes, and functions must have documentation
  - Only `numpy` and `tensorflow` are allowed for imports unless otherwise noted
  - All files must be executable

## Usage

### Applying Style Transfer

To apply style transfer to your own images:

python scripts/style_transfer.py --content images/your_content.jpg --style images/your_style.jpg --output output/stylized_image.jpg
