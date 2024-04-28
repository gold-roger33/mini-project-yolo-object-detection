import cv2
from ultralytics import YOLO
import pyttsx3

model = YOLO("yolov8n.pt")
engine = pyttsx3.init()



cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame,stream=True, verbose=False, show=True, conf=0.7)

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
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
engine.stop()