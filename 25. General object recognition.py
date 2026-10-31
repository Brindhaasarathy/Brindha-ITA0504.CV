
import cv2

# Load pre-trained YOLO model
config = "yolov3.cfg"
weights = "yolov3.weights"
classes_file = "coco.names"

# Load class names
with open(classes_file, "r") as f:
    classes = f.read().strip().split("\n")

# Load YOLO network
net = cv2.dnn.readNetFromDarknet(config, weights)

# Read input image
img = cv2.imread("watch.jpg")

if img is None:
    print("Image not found!")
    exit()

height, width = img.shape[:2]

# Create blob from image
blob = cv2.dnn.blobFromImage(
    img, 1/255.0, (416, 416),
    swapRB=True, crop=False
)

net.setInput(blob)

# Get output layer names
layer_names = net.getLayerNames()
output_layers = [
    layer_names[i - 1]
    for i in net.getUnconnectedOutLayers().flatten()
]

# Perform object detection
outputs = net.forward(output_layers)

boxes = []
confidences = []
class_ids = []

# Process detection results
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = scores.argmax()
        confidence = scores[class_id]

        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Remove duplicate detections
indexes = cv2.dnn.NMSBoxes(
    boxes, confidences, 0.5, 0.4
)

# Draw bounding boxes
for i in indexes.flatten():
    x, y, w, h = boxes[i]
    label = classes[class_ids[i]]

    cv2.rectangle(
        img, (x, y), (x+w, y+h),
        (0, 255, 0), 2
    )

    cv2.putText(
        img, label, (x, y-10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7, (0, 255, 0), 2
    )

    print("Detected Object:", label)

# Display result
cv2.imshow("Watch Object Recognition", img)

# Save output
cv2.imwrite("watch_output.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
