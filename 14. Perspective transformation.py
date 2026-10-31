import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

# Get image dimensions
rows, cols = img.shape[:2]

# Define four points in original image
pts1 = np.float32([[50, 50], [300, 50],
                   [50, 300], [300, 300]])

# Define four destination points
pts2 = np.float32([[10, 100], [250, 50],
                   [100, 350], [300, 300]])

# Calculate perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
result = cv2.warpPerspective(img, matrix, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", result)

# Save output image
cv2.imwrite("perspective_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
