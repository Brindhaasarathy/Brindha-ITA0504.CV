import cv2
import numpy as np

def background_subtraction(image_path):
    # Read the input image
    img = cv2.imread(r"C:\Users\brind\OneDrive\Documents\Computer vision lab\cv image.jpg")

    if img is None:
        print("Image not found!")
        return

    # Convert image from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define background color range
    lower = np.array([0, 0, 0])
    upper = np.array([180, 255, 100])

    # Create mask based on color levels
    mask = cv2.inRange(hsv, lower, upper)

    # Remove background
    result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Background Removed", result)

    # Save output
    cv2.imwrite("background_removed.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function call
background_subtraction("image.jpg")
