import cv2

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)

    # Count faces
    print("Number of faces detected:", len(faces))

    # Display image
    cv2.imshow("Face Detection", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
