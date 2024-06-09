import cv2

# Replace with your ESP32-CAM IP address
esp32_cam_url = 'http://192.168.0.105:81/stream'

# Initialize video capture with the ESP32-CAM stream URL
cap = cv2.VideoCapture(esp32_cam_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Error: Could not read frame.")
        break

    # Rotate the frame by 90 degrees to the left
    frame_rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Display the resulting frame
    cv2.imshow('ESP32-CAM Stream', frame_rotated)

    # Exit the stream on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()