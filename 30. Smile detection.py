import cv2

# Load the image
img = cv2.imread("image.jpg")

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load smile cascade classifier
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

# Detect smiles
smiles = smile_cascade.detectMultiScale(
    gray,
    scaleFactor=1.8,
    minNeighbors=20,
    minSize=(25, 25)
)

# Draw rectangles around detected smiles
for (x, y, w, h) in smiles:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the output
cv2.imshow("Smile Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
