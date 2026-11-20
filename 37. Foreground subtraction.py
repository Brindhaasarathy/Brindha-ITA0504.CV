import cv2
import numpy as np

def foreground_subtraction(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found!")
        return

    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define foreground color range
    lower = np.array([0, 0, 100])
    upper = np.array([180, 255, 255])

    # Create mask based on color levels
    mask = cv2.inRange(hsv, lower, upper)

    # Subtract foreground
    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Foreground Subtracted", result)

    # Save output image
    cv2.imwrite("foreground_removed.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function call
foreground_subtraction("image.jpg")
