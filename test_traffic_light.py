# from ultralytics import YOLO
# import cv2

# # تحميل النموذج المدرب
# model = YOLO("C:\\Mahmoud_Saeed\\My_projects\\project_graduation\\traffic_light\\runs\\detect\\train\\weights\\best.pt")

# # تحميل الصورة للاختبار
# # image_path = "C:\\Mahmoud_Saeed\\project_graduation\\traffic_light\\cinTA_v2\\test\\images\\traffic-light-87-_jpg.rf.efc716437308b5ef084b2cf5db9af90c.jpg"
# # image_path = "C:\\Mahmoud_Saeed\\project_graduation\\traffic_light\\cinTA_v2\\test\\images\\traffic-light-128-_jpg.rf.43db6eadbd7a950bbcfd7f1f12959440.jpg"
# image_path = "C:\\Mahmoud_Saeed\\My_projects\\project_graduation\\traffic_light\\cinTA_v2\\test\\images\\traffic-light-87-_jpg.rf.efc716437308b5ef084b2cf5db9af90c.jpg"
# image = cv2.imread(image_path)  # ✅ تم إصلاح الخطأ

# # التحقق من تحميل الصورة بشكل صحيح
# if image is None:
#     raise ValueError("❌ خطأ: تعذر تحميل الصورة، تأكد من صحة المسار.")

# # تشغيل النموذج على الصورة
# results = model(image)  # ✅ استخدم الصورة المحملة بدلاً من مسارها

# # تعيين خريطة الألوان الصحيحة
# color_map = {0: "Green - go🚦✅", 2: "Yellow - wait ⚠️", 1: "Red - stop ⛔"}
# detected_classes = set()

# # استخراج البيانات من نتائج النموذج
# for result in results:
#     for box in result.boxes:
#         class_id = int(box.cls.item())  # ✅ تأكد من استخراج معرف الفئة بشكل صحيح
#         detected_classes.add(class_id)

# # اتخاذ القرار بناءً على جميع الإشارات المكتشفة
# if not detected_classes:
#     decision = "🚦 No traffic light"
# elif 1 in detected_classes:  # إذا كانت الإشارة حمراء، الأولوية للتوقف
#     decision = color_map[1]
# elif 2 in detected_classes:  # إذا كانت الإشارة صفراء، الأولوية للانتظار
#     decision = color_map[2]
# else:  # إذا لم يكن هناك سوى الإشارة الخضراء
#     decision = color_map[0]

# # عرض النتيجة
# print(f"🛑 Decision :  {decision}")

# # ✅ حل المشكلة: عرض الصورة مع النتائج بشكل صحيح
# if results:
#     results[0].show()


import cv2
from ultralytics import YOLO

# تحميل النموذج المدرب
model = YOLO("C:\\Mahmoud_Saeed\\My_projects\\project_graduation\\traffic_light\\runs\\detect\\train\\weights\\best.pt")

# تعيين خريطة الألوان الصحيحة
color_map = {0: "Green - go 🚦✅", 2: "Yellow - wait ⚠️", 1: "Red - stop ⛔"}

# فتح كاميرا الويب أو تشغيل فيديو (ضع مسار الفيديو هنا إذا كنت تريد استخدام فيديو)
video_source = 0  # استخدم 0 لكاميرا الويب أو ضع مسار ملف فيديو مثلاً: "video.mp4"
cap = cv2.VideoCapture(video_source)

# التحقق من نجاح فتح الكاميرا / الفيديو
if not cap.isOpened():
    print("❌ خطأ: تعذر فتح كاميرا الويب أو ملف الفيديو.")
    exit()

while True:
    # قراءة الإطار الحالي من الكاميرا / الفيديو
    ret, frame = cap.read()
    
    # إذا لم يتم التقاط الإطار، اخرج من الحلقة
    if not ret:
        print("❌ خطأ: تعذر التقاط الإطار. إنهاء التطبيق...")
        break

    # تشغيل YOLO على الإطار الحالي
    results = model(frame)

    detected_classes = set()

    # استخراج البيانات من نتائج النموذج
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls.item())  # استخراج معرف الفئة
            detected_classes.add(class_id)

            # استخراج إحداثيات الصندوق وإضافتها إلى الصورة
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            label = color_map.get(class_id, "Unknown")
            color = (0, 255, 0) if class_id == 0 else (0, 255, 255) if class_id == 2 else (0, 0, 255)

            # رسم الصندوق حول الإشارة الضوئية
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # اتخاذ القرار بناءً على الإشارات المكتشفة
    if not detected_classes:
        decision = "🚦 No traffic light"
    elif 1 in detected_classes:  # إذا كانت الإشارة حمراء، الأولوية للتوقف
        decision = color_map[1]
    elif 2 in detected_classes:  # إذا كانت الإشارة صفراء، الأولوية للانتظار
        decision = color_map[2]
    else:  # إذا لم يكن هناك سوى الإشارة الخضراء
        decision = color_map[0]

    # عرض القرار في أعلى الإطار
    cv2.putText(frame, f"Decision: {decision}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)

    # عرض الفيديو مع النتائج
    cv2.imshow("Real-Time Traffic Light Detection", frame)

    # الضغط على "Q" لإنهاء التطبيق
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# إغلاق الكاميرا وإغلاق جميع النوافذ
cap.release()
cv2.destroyAllWindows()
