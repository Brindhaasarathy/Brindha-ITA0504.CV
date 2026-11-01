import cv2

def reverse_video(input_video, output_video):

    # Read the input video
    cap = cv2.VideoCapture(input_video)

    frames = []

    # Store all video frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    # Get video properties
    height, width = frames[0].shape[:2]
    fps = 20

    # Create output video
    out = cv2.VideoWriter(
        output_video,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    # Write frames in reverse order
    for frame in reversed(frames):
        out.write(frame)

    out.release()

    print("Reverse video created successfully!")


# Function call
reverse_video("input.mp4", "reverse.mp4")
