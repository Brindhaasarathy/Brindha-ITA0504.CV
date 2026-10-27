import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread(r"C:\Users\brind\OneDrive\Documents\Computer vision lab\cv image.jpg")

# Convert the image from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define a function to analyze the histogram
def analyze_histogram(img):
    colors = ('r', 'g', 'b')

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)

    plt.title("Image Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.show()

# Call the function
analyze_histogram(img)
