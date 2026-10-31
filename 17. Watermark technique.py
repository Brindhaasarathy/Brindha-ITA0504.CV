import cv2

# Read original and watermark images
img = cv2.imread('original.jpg')
watermark = cv2.imread('watermark.png')

# Resize watermark
watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))

# Blend images
result = cv2.addWeighted(img, 0.7, watermark, 0.3, 0)

# Save watermarked image
cv2.imwrite('watermarked.jpg', result)

# Display images
cv2.imshow('Original Image', img)
cv2.imshow('Watermark Image', watermark)
cv2.imshow('Watermarked Image', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
