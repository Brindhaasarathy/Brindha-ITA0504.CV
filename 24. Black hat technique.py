
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg")

if img is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Perform Black Hat operation
blackhat = cv2.morphologyEx(
    gray,
    cv2.MORPH_BLACKHAT,
    kernel
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Black Hat Result", blackhat)

# Save output image
cv2.imwrite("blackhat_output.jpg", blackhat)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Black Hat operation completed successfully!")
