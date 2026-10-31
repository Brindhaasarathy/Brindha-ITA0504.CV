import cv2
import numpy as np

def rotate_y_axis(image_path, output_path, angle=270):
    # Load image
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found!")

    h, w = img.shape[:2]

    # Convert angle to radians
    theta = np.radians(angle)

    # Camera focal length
    f = w

    # Camera intrinsic matrix
    K = np.array([
        [f, 0, w / 2],
        [0, f, h / 2],
        [0, 0, 1]
    ], dtype=np.float32)

    # Rotation matrix around Y-axis
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ], dtype=np.float32)

    # Homography transformation
    H = K @ R @ np.linalg.inv(K)

    # Apply perspective transformation
    rotated = cv2.warpPerspective(img, H, (w, h))

    # Save result
    cv2.imwrite(output_path, rotated)

    print("Image rotated successfully!")

# Example
rotate_y_axis("input.jpg", "output.jpg", 270)
