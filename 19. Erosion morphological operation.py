
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert image into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert grayscale image into binary image
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion operation
erosion = cv2.erode(
    binary, kernel, iterations=1
)

# Display original image
cv2.imshow("Original Image", img)

# Display binary image
cv2.imshow("Binary Image", binary)

# Display eroded image
cv2.imshow("Erosion Image", erosion)

# Save the output image
cv2.imwrite("erosion_output.jpg", erosion)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
