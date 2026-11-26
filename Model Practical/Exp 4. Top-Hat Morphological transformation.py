import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create structuring element
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (9, 9)
    )

    # Apply top-hat transformation
    tophat = cv2.morphologyEx(
        gray, cv2.MORPH_TOPHAT, kernel
    )

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Top-Hat Image", tophat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
