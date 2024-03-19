import cv2
from ultralytics import YOLO

video_path = 'square.mp4'
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

#frame interval for every 2 seconds
frame_interval = int(fps * 2)


video_frames = []
success, frame = cap.read()


while success:
    
    video_frames.append(frame)

    # Move to the next frame after 2 seconds
    for _ in range(frame_interval):
        success, frame = cap.read()


cap.release()
print(f"Total frames extracted: {len(video_frames)}")



model = YOLO("yolov8n.pt")


for i in range(len(video_frames)):
    results = model(video_frames[i],verbose=False, show=True, conf=0.8)
 
    for result in results:
        cls = result.boxes.cls
        size = result.boxes.xyxy
        for c, s in zip(cls, size):
            class_name = result.names[int(c)]
            x_center = (s[0] + s[2]) / 2  # Calculate the x-coordinate of the bounding box center
            image_width = video_frames[i].shape[1]  # Width of the frame

            if x_center < image_width / 2:
                position = "left"
            elif x_center > image_width / 2:
                position = "right"
            else:
                position = "center"
            print(f"{class_name} is located on the {position} side")
 

cv2.waitKey(10000)


#cv2.destroyAllWindows()
