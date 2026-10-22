import cv2

# Read the captured video
cap = cv2.VideoCapture(r"C:\Users\brind\OneDrive\Documents\Computer vision lab\cv video.mp4")

if not cap.isOpened():
    print("Error: Video not found!")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Display video in normal speed
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Normal Speed", frame)

        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cap = cv2.VideoCapture("video.mp4")

    # Display video in slow motion
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Slow Motion", frame)

        if cv2.waitKey(int(2000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cap = cv2.VideoCapture("video.mp4")

    # Display video in fast motion
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Fast Motion", frame)

        if cv2.waitKey(int(500 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
