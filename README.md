# 🚦 Traffic Light Detection — YOLOv8 Project

![Traffic Light Detection]([https://github.com/Mahmoud3301/traffic_light/blob/main/4.mp4](https://github.com/Mahmoud3301/traffic_light/blob/main/traffic.jpeg))

[![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-blue?logo=python)]()
[![Dataset](https://img.shields.io/badge/Dataset-CinTA_v2-orange)]()
[![Framework](https://img.shields.io/badge/Framework-PyTorch-lightblue)]()

**Traffic Light Detection** is a computer vision project designed to detect and classify traffic lights in real-time using the **YOLOv8** model.  
It leverages the **CinTA_v2 dataset** and is implemented with **PyTorch**, making it suitable for traffic monitoring, autonomous driving, and intelligent transportation systems.

---

## ✨ Features

- 🚦 **Real-Time Traffic Light Detection**
  - Detects Red, Yellow, and Green traffic lights.
  - Works on video inputs and real-time streams.

- 🧠 **Powered by YOLOv8**
  - Trained on **CinTA_v2** dataset.
  - High accuracy and robust performance in various conditions.

- 💻 **Cross-Platform Testing**
  - Compatible with video files and webcam feeds.
  - Can be extended for live traffic applications.

---

## 🏗️ Project Flow

🎥 Input Video → YOLOv8 Detection → Traffic Light Classification → Bounding Box Display → Output Video/Stream

---

## 🛠️ Technologies Used

- YOLOv8 (Ultralytics)  
- PyTorch  
- Python  
- CinTA_v2 Dataset  

---

## 🚀 Future Improvements

- Real-time detection with live camera feed.  
- Multi-class detection for other traffic signs.  
- Deployment as a web or mobile application.  
- Integration with autonomous driving pipelines.  

---

## 👨‍💻 Developed By

Mahmoud3301

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Mahmoud3301/traffic_light.git
cd traffic_light

# Install dependencies
pip install -r requirements.txt

# Run the detection on a video
python test_traffic_light.py --weights yolov8n.pt --source test1.mp4
