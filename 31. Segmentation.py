
import cv2

# Read the input image
img = cv2.imread(r"C:\Users\student\Downloads\eye.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display original image
cv2.imshow("Original Image", img)

# Display segmented image
cv2.imshow("Image Segmentation", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
