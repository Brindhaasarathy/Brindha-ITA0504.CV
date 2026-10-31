import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread('input.jpg')

# Convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Rotate image by 180 degrees
rotated_img = cv2.rotate(img, cv2.ROTATE_180)

# Display original and rotated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rotated_img)
plt.title("180 Degree Rotation")
plt.axis('off')

plt.show()

# Save rotated image
plt.imsave('rotated_180.jpg', rotated_img)
