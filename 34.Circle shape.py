
import cv2
import numpy as np

def create_circle():
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Find center of image
    center = (width//2, height//2)

    # Draw circle
    radius = min(height, width)//4
    cv2.circle(img, center, radius, (0, 0, 255), 3)

    # Display image
    cv2.imshow("Circle", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_circle()
