import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert color image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    # Save grayscale image
    cv2.imwrite("grayscale.jpg", gray)

    # Verify saving
    if cv2.imread("grayscale.jpg") is not None:
        print("Grayscale image saved successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
