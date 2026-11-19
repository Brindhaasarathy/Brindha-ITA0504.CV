
import cv2
import numpy as np

def create_rectangle():
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw rectangle
    cv2.rectangle(img, (100, 100), (width-100, height-100), (0, 0, 255), 3)

    # Display image
    cv2.imshow("Rectangle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_rectangle()
