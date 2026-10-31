
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg")

if img is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert into binary image
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create structuring element
kernel = np.ones((5, 5), np.uint8)

# Perform Closing operation
closing = cv2.morphologyEx(
    binary,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=1
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Closing Result", closing)

# Save output image
cv2.imwrite("closing_output.jpg", closing)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Closing operation completed successfully!")
