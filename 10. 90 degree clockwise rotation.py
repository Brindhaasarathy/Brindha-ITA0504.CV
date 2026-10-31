import cv2
import matplotlib.pyplot as plt

# Read the input image
img = cv2.imread('input.jpg')

# Convert BGR to RGB for displaying with Matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Rotate image 90 degrees clockwise
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# Display original and rotated images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rotated_img)
plt.title("90 Degree Clockwise Rotation")
plt.axis('off')

plt.show()

# Save the rotated image
cv2.imwrite('rotated_image.jpg',
            cv2.cvtColor(rotated_img, cv2.COLOR_RGB2BGR))
