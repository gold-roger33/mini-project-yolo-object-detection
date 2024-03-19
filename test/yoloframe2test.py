from ultralytics import YOLO
import cv2

def process_frame(frame, confidence_threshold=0.8, show=False):
    
    results = model(frame, conf=confidence_threshold)
    print('results is alsdhjadha',results)

"""
    # Process and print results for each frame
    for det in results.xyxy[0].numpy():
        confidence = det[4]

        # Check if confidence is greater than the threshold
        if confidence > confidence_threshold:
            class_label = model.names[int(det[5])]
            object_info = f"{int(confidence * 100)}% {class_label}, Box: {det[:4].tolist()}"
            print(object_info)

    # Display the frame with bounding boxes if show is True
    if show:
        results.show()
"""
# Initialize YOLO model
model = YOLO("yolov5s.pt")

# Assume you have a video capture object 'cap'
cap = cv2.VideoCapture("square.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Process each frame using the custom function
    process_frame(frame, confidence_threshold=0.8, show=True)

# Release resources
cap.release()
cv2.destroyAllWindows()
