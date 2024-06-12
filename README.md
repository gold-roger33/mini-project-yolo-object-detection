# Object Detection System for Visually Impaired: Raspberry Pi & Python(Mini Project)

This repository is the code for my  mini project that demonstrates real-time object detection using the YOLO (You Only Look Once) model in rasperry pi 4B.
The project is designed to assist the visually impaired by detecting and announcing objects in their surroundings.



## Features

- Real-time object detection using YOLO model
- Video input from the camera module/webcam
- Detection of various classes of objects
- Announcement of detected objects and their positions using text-to-speech engine

## Requirements

- Python 3.12
- ultralytics library
- pyttsx3 library
- Pre-trained YOLO model (yolov8n.pt)
- camera module (you can use web camera)
- rasperry pi(you can run in pc)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/gold-roger33/mini-project-yolo-object-detection.git
    ```

2. Install the required libraries:

    ```bash
    pip install ultralytics pyttsx3
    ```

3. Run the main script:

    ```bash
    cd final code
    python livecam.py
    ```
4. Point the camera module towards the surroundings and listen to the announcements of detected objects.


## Additionals 

There is a test folder which i used to test some features like detecting objects from video

## credits

- Ultralytics YOLO: [Documentation](https://docs.ultralytics.com/quickstart/)

