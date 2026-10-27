```python
import cv2

# Read the input image
img = cv2.imread("image.jpg")

# Check if the image exists
if img is None:
    print("Image not found")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Gaussian Blur Image", blur)

    # Save the blurred image
    cv2.imwrite("blurred_image.jpg", blur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
