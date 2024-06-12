# This script performs real-time object detection using a YOLO model on video input from the default webcam.
# The video input is processed directly by the YOLO model, without explicitly using OpenCV for video capture, reducing processing delays.
# The detected objects and their positions relative to the frame's center are announced using a text-to-speech engine.

from ultralytics import YOLO
import pyttsx3


# Initialize the YOLO model
model = YOLO("yolov8n.pt")
results = model(source=0,stream=True, verbose=False, show=True, conf=0.8)

#initialising pyttsx3 for text to speach
engine = pyttsx3.init()


for result in results:
    cls = result.boxes.cls
    size = result.boxes.xyxy
    frame_width = result.orig_shape[1] #640*640

    for c, s in zip(cls, size):
        class_name = result.names[int(c)]
            
        x_center = (s[0] + s[2]) / 2
        #print(image_width)


        # Determine the position of the object relative to the frame's center
        if x_center < frame_width / 2:
            position = "left"
        elif x_center > frame_width / 2:
            position = "right"
        else:
            position = "center"

        # Generate the text to be spoken
        text = f"{class_name} is located on the {position} side"
        print(text)
        engine.say(text)
        engine.runAndWait()


# Stop the pyttsx3 engine
engine.stop()          