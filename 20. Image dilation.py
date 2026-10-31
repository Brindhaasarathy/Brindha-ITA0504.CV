
import cv2
import numpy as np

# Read the input image
img = cv2.imread("input.jpg")

if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert image to binary
ret, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# Create a structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(
    binary,
    kernel,
    iterations=1
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Dilated Image", dilated)

# Save the dilated image
cv2.imwrite("dilated_output.jpg", dilated)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Dilation performed successfully!")
