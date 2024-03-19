from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO("yolov5s.pt")

# Assume you have a video capture object 'cap'
cap = cv2.VideoCapture("square.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    #results = model(frame)

    result= model("square.mp4",show=True, conf=0.8)
    #print("REsult =", result)
    

        

    '''
    for det in result.xyxy[0].numpy():
        confidence = det[4]

        # Check if confidence is greater than 80%
        if confidence > 0.8:
            class_label = model.names[int(det[5])]
            object_info = f"{int(confidence * 100)}% {class_label}, Box: {det[:4].tolist()}"
            print(object_info)
    
        '''
'''
    # Iterate over predictions for each frame
    for prediction in results[0]:  # Access the first element of the list
        # Access individual attributes of the prediction
        label = prediction[-1]
        confidence = prediction[4]

        # Check if confidence is greater than 75%
        if confidence > 0.75:
            # Print or process the information as needed
            print(f"Label: {label}, Confidence: {confidence}")

    # Display the frame with bounding boxes
    results.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

'''

#        print(object_info)

cap.release()
cv2.destroyAllWindows()
