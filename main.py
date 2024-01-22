import cv2
import os

def webcam_background_recording(output_file="output.avi"):
    # Open the webcam (0 indicates the default camera, you can change it if you have multiple cameras)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Get the video width and height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Try 'MJPG' if 'XVID' doesn't work
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    recording = True

    while recording:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Write the frame to the output video file if recording
        if recording:
            out.write(frame)

        # Break the loop when 'esc' key is pressed
        key = cv2.waitKey(1)
        if key == 27:  # 27 is the ASCII code for the 'esc' key
            break

    # Release the webcam and release the video writer
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_file = "output.avi"
    print("Recording started. Press 'esc' to stop and save the recording.")
    webcam_background_recording(output_file)
    print(f"Recording saved to {output_file}")
