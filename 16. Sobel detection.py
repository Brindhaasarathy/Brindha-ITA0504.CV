import cv2

# Read input image
img = cv2.imread('image.jpg', 0)

# Apply Sobel filter in X direction
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter in Y direction
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine both directions
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Edge Detection', sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
