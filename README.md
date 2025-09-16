## My Data is called cinTA_v2.v1i.yolov8
## https://universe.roboflow.com/wawan-pradana/cinta_v2/dataset/1

# 🚦 Traffic Light Detection with YOLOv8

![Traffic Light Detection](https://github.com/Mahmoud3301/traffic_light/blob/main/4.mp4)

[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-blue?logo=python)]()
[![Dataset](https://img.shields.io/badge/Dataset-CinTA_v2-orange)]()
[![Framework](https://img.shields.io/badge/Framework-PyTorch-lightblue)]()

**Traffic Light Detection with YOLOv8** is an advanced computer vision project aimed at detecting and classifying traffic lights in real-time using the latest YOLOv8 model. This project leverages the **CinTA_v2** dataset and is implemented using **PyTorch**.

---

## 🎯 Objective

The goal of this project is to develop a robust system capable of accurately detecting traffic lights in various traffic conditions. By training the YOLOv8 model on the **CinTA_v2** dataset, the system can identify traffic light states (Red, Yellow, Green) in real-time, which is crucial for intelligent traffic management systems.

---

## 📂 Project Structure

traffic_light/
├── runs/
│ ├── detect/
│ ├── train/
├── 4.mp4
├── README.md
├── cinta.yaml
├── test1.mp4
├── test_traffic_light.py
├── traffic_light_training.py
├── yolo11m.pt
├── yolo11s.pt
├── yolov12m.pt
└── yolov8n.pt


## 🧪 Key Components

- **`traffic_light_training.py`**: Script to train the YOLOv8 model on the CinTA_v2 dataset.
- **`test_traffic_light.py`**: Testing script to evaluate the model's performance on video inputs.
- **`cinta.yaml`**: Dataset configuration file for YOLOv8.
- **Model Weights**: Pre-trained weights for different YOLOv8 versions (`yolo11m.pt`, `yolo11s.pt`, `yolov12m.pt`, `yolov8n.pt`).

---

📈 Results

The model demonstrates high accuracy in detecting traffic lights under various conditions. For a visual demonstration, refer to the following video:

🔧 Future Enhancements

Real-time Detection: Implement real-time traffic light detection using a webcam.

Multi-Class Detection: Extend the model to detect other traffic signs and signals.

Deployment: Develop a web or mobile application for real-world deployment.

👨‍💻 Developed By

Mahmoud-Saeed


## 📦 Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Mahmoud3301/traffic_light.git
   cd traffic_light



