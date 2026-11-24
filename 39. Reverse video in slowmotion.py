import cv2

cap = cv2.VideoCapture(r"C:\Users\SAIL\Downloads\128455-741454873.mp4")

if not cap.isOpened():
    print("Video not found")
    exit()

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion Video", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
