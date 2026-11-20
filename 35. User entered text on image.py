import cv2

def add_text(image_path):
    # Read the image
    img = cv2.imread(r"C:\Users\brind\OneDrive\Documents\Computer vision lab\cv image.jpg")

    if img is None:
        print("Image not found!")
        return

    # Get text from the user
    text = input("Enter the text to display on the image: ")

    # Add text to the image
    cv2.putText(img, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Image with Text", img)

    # Save the output image
    cv2.imwrite("output.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function call
add_text("image.jpg")
