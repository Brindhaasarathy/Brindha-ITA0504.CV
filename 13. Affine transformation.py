import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

# Get image dimensions
rows, cols = img.shape[:2]

# Define three points
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# Define destination points
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Calculate affine transformation matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
result = cv2.warpAffine(img, matrix, (cols, rows))

# Display original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", result)

# Save transformed image
cv2.imwrite("affine_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
