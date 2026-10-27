```python
import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display original and outline images
    cv2.imshow("Original Image", img)
    cv2.imshow("Outline Image", edges)

    # Save the outline image
    cv2.imwrite("outline_image.jpg", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
```
