
import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('image.jpg')

if img is None:
    print("Error: Image not found!")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize to a bigger size
    bigger = cv2.resize(img, None, fx=2, fy=2)

    # Resize to a smaller size
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Display images
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(bigger)
    plt.title("Bigger Image")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(smaller)
    plt.title("Smaller Image")
    plt.axis("off")

    plt.show()
