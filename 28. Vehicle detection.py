
import cv2

# Load pre-trained vehicle cascade classifier
vehicle_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_car.xml'
)

# Open video file or webcam
# Use 0 for webcam
cap = cv2.VideoCapture("vehicles.mp4")

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

while True:
    # Read each video frame
    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (800, 600))

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles
    vehicles = vehicle_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(40, 40)
    )

    # Process detected vehicles
    for (x, y, w, h) in vehicles:

        # Draw bounding box
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Calculate center location
        center_x = x + w // 2
        center_y = y + h // 2

        # Display vehicle label
        cv2.putText(
            frame,
            "Vehicle",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # Display coordinates
        coordinates = f"X:{center_x}, Y:{center_y}"

        cv2.putText(
            frame,
            coordinates,
            (x, y + h + 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

    # Display total vehicle count
    cv2.putText(
        frame,
        f"Vehicles Detected: {len(vehicles)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Display output frame
    cv2.imshow("Vehicle Detection and Localization", frame)

    # Press Q to exit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
