import cv2
import face_recognition
import psutil
import os
import time
from datetime import datetime

# Load authorized users
authorized_users = {
    "user1": "path_to_user1_image.jpg",
    "user2": "path_to_user2_image.jpg"
}

# Encode authorized faces
authorized_encodings = {}
for name, image_path in authorized_users.items():
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    authorized_encodings[name] = encoding

# Capture a still image
def capture_still_image():
    cap = cv2.VideoCapture(0)  # Initialize the camera
    if not cap.isOpened():
        raise Exception("Could not open camera.")
    
    ret, frame = cap.read()  # Capture a single frame
    cap.release()  # Release the camera immediately
    if ret:
        return frame
    else:
        raise Exception("Could not capture frame.")

# Facial recognition
def recognize_face():
    frame = capture_still_image()  # Capture a still image
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for encoding in face_encodings:
        for name, authorized_encoding in authorized_encodings.items():
            if face_recognition.compare_faces([authorized_encoding], encoding)[0]:
                return name, frame  # Return the frame along with the name
    return None, frame  # Return the frame even if no face is recognized

# Save unauthorized access image
def save_unauthorized_image(frame):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = f"unauthorized_access_{timestamp}.jpg"
    cv2.imwrite(image_path, frame)
    print(f"Unauthorized access detected. Image saved as {image_path}")

# Monitor applications
def monitor_applications(app_name):
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == app_name:
                return True
        time.sleep(0.5)  # Add a 0.5s delay here

# Main loop
def main():
    app_name = "chrome.exe"  # Example application
    while True:
        if monitor_applications(app_name):
            user, frame = recognize_face()
            if user not in authorized_users:
                save_unauthorized_image(frame)  # Save the image of the unauthorized user
                os.system(f"taskkill /f /im {app_name}")  # Windows command to kill process
                print(f"Unauthorized access detected. {app_name} has been shut down.")
            else:
                print(f"Authorized user {user} detected.")

if __name__ == "__main__":
    main()
