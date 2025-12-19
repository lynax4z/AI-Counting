import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
result = model('/Volumes/Macintosh HD/Users/vencent/AICounting/yolo_model/20221113_154950.jpg', show=True)
show = result[0].plot()

cv2.imshow('test', show)
cv2.waitKey(0)
cv2.destroyAllWindows()

