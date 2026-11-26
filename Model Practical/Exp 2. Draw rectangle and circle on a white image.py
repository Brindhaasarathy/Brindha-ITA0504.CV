import cv2
import numpy as np

# Create a blank white image
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw rectangle
cv2.rectangle(img, (50, 50), (250, 200), (0, 0, 255), 3)

# Draw circle
cv2.circle(img, (350, 150), 80, (255, 0, 0), 3)

# Get text from user
text = input("Enter text: ")

# Insert text
cv2.putText(img, text, (50, 300),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 0), 2)

# Display image
cv2.imshow("Drawing Canvas", img)

# Save image
cv2.imwrite("drawing.jpg", img)

print("Image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
