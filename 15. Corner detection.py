import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert image to float32
gray = np.float32(gray)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray, 2, 3, 0.04)

# Mark detected corners
img[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display original and corner detected image
cv2.imshow("Harris Corner Detection", img)

# Save output image
cv2.imwrite("harris_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
