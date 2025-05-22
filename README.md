# Road Sign Recognition Project

## Overview
The Road Sign Recognition project is a real-time detection system designed to recognize road signs across 43 different classes. The project leverages the YOLOv5 model, which is trained on the [GTSRB - German Traffic Sign Recognition Benchmark](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) dataset.

This system can be used to improve road safety and assist autonomous driving by identifying and interpreting road signs in real-time through a camera feed.

## Project Structure
The project folder `road-sign-recognition` includes the following subdirectories:

1. **`model`**: Contains the trained YOLOv5 model weights (`best.pt` and `last.pt`).
2. **`src`**: Contains the source code for running the project.

## Features
- Real-time detection and classification of road signs.
- Recognizes 43 distinct classes of road signs.
- Easy-to-use and customizable codebase.

## Dataset
The model is trained on the [GTSRB - German Traffic Sign Recognition Benchmark](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) dataset. This dataset contains over 50,000 images of road signs across 43 different classes, providing a robust training foundation for road sign recognition tasks.

## Requirements
Ensure you have Python installed on your system. The dependencies for the project are listed in the `requirements.txt` file.

### Steps to Install Dependencies
1. Open a terminal or command prompt.
2. Navigate to the project directory:
   
   ```
   cd road-sign-recognition
   ```
4. Install the dependencies using the following command:
   
   ```
   pip install -r requirements.txt
   ```

## How to Run the Project
1. Ensure you have a webcam or camera feed available.
2. Run the main script located in the **`src`** folder to start the real-time detection:
   
   ```
   python src/main.py
   ```
3. The system will start detecting and classifying road signs in real-time. Press **`q`** to quit the application.

## Model Training Results
![Model Training Results](https://github.com/ayushgayakwad/road-sign-recognition/blob/main/model/results.png)

## Research Publication
This project is published as a research paper in the *Journal of Emerging Technologies and Innovative Research (JETIR)*: 

**Title:** Road Sign Recognition using YOLO & GTSRB  
**Journal:** JETIR (Volume 12, Issue 5, May 2025)  
**Published Paper ID:** JETIR2505760  
**Published Paper Link:** [JETIR2505760 - Road Sign Recognition using YOLO & GTSRB](https://www.jetir.org/view?paper=JETIR2505760)

## Acknowledgements
- [YOLOv5](https://github.com/ultralytics/yolov5) for object detection.
- [GTSRB Dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) for providing the benchmark dataset for training.
  
