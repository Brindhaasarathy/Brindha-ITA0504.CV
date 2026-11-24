
import cv2
import pytesseract
import tempfile
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\SAIL\Downloads\ocr_experiment40_video.mp4"

os.environ["TEMP"] = tempfile.gettempdir()
os.environ["TMP"] = tempfile.gettempdir()

cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Video not found")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    try:
        text = pytesseract.image_to_string(gray)

        if text.strip():
            print("Extracted Text:", text)

    except Exception as e:
        print("OCR Error:", e)

    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
