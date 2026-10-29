import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread(r"C:\Users\student\OneDrive\Documents\computer vision lab\images.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Convert BGR to RGB for displaying
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create a 5x5 kernel
    kernel = np.ones((5, 5), np.uint8)

    # Perform image dilation
    dilated_img = cv2.dilate(
        img, kernel, iterations=1
    )

    # Convert dilated image to RGB
    dilated_rgb = cv2.cvtColor(
        dilated_img, cv2.COLOR_BGR2RGB
    )

    # Display original and dilated images
    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(dilated_rgb)
    plt.title("Dilated Image")
    plt.axis("off")

    plt.show()
