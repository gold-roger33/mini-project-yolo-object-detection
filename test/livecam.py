"""
almost completed upto detecting objects and preficting the onject
with a confidence of  80% and determining the position of objects 
*NEED TO ADD VOICE GENERATION

"""

from ultralytics import YOLO
import pyttsx3

model = YOLO("yolov8n.pt")
results = model(source=0,stream=True, verbose=False, show=True, conf=0.8)

engine = pyttsx3.init()


for result in results:
    cls = result.boxes.cls
    size = result.boxes.xyxy
    frame_width = result.orig_shape[1] #640*640

    for c, s in zip(cls, size):
        class_name = result.names[int(c)]
            
        x_center = (s[0] + s[2]) / 2
        #print(image_width)
            
        if x_center < frame_width / 2:
            position = "left"
        elif x_center > frame_width / 2:
            position = "right"
        else:
            position = "center"

        text = f"{class_name} is located on the {position} side"
        print(text)
        engine.say(text)
        engine.runAndWait()



engine.stop()          