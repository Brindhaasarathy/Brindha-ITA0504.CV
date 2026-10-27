import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\brind\OneDrive\Documents\Computer vision lab\cv image.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded_img = cv2.erode(img, kernel, iterations=1)

    # Display the original and eroded images
    cv2.imshow("Original Image", img)
    cv2.imshow("Eroded Image", eroded_img)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
