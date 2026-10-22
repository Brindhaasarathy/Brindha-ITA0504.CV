import cv2

# Read the image
img = cv2.imread(r"C:\Users\brind\OneDrive\Documents\Computer vision lab\cv image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Display the original image
cv2.imshow("Original Image", gray)

# Display the equalized image
cv2.imshow("Histogram Equalized Image", equalized)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
