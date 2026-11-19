
import cv2
import numpy as np

def create_image():
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Box size (1/10th of image)
    h = height // 10
    w = width // 10

    # Black box - Top Left
    img[0:h, 0:w] = [0, 0, 0]

    # Blue box - Top Right
    img[0:h, width-w:width] = [255, 0, 0]

    # Green box - Bottom Left
    img[height-h:height, 0:w] = [0, 255, 0]

    # Red box - Bottom Right
    img[height-h:height, width-w:width] = [0, 0, 255]

    # Display image
    cv2.imshow("Colored Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

create_image()
