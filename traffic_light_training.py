from ultralytics import YOLO
import torch

# التأكد مما إذا كان CUDA متاحًا واستخدامه
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# تحميل نموذج YOLOv8 الأساسي أو نموذج مخصص
model = YOLO("yolov8n.pt")  # يمكن تغييره إلى yolov8m.pt أو yolov8l.pt حسب الحاجة

# تدريب النموذج على مجموعة بيانات CinTA_v2
model.train(data="C:\\Mahmoud_Saeed\\project_graduation\\traffic_light\\cinta.yaml",
            epochs=50,  # عدد التكرارات
            batch=8,  # حجم الدفعة
            imgsz=640,  # حجم الصور المدخلة
            device=device)  # استخدام الجهاز المناسب

# حفظ النموذج المدرب
model.export(format="onnx")  # تصدير النموذج إلى ONNX لاستخدامه لاحقًا


