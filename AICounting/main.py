import cv2
import optimize
import time

optimize.loadCascade('/Volumes/Macintosh HD/Users/vencent/AICounting/haarcascade_frontalface_alt2.xml')
#optimize.loadCascade('/Volumes/Macintosh HD/Users/vencent/AICounting/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print('camera is not opened')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("can't receive the frame")
        break
    boxes = optimize.detect(frame)
    count = len(boxes)
    cv2.putText(frame, f'count : {count}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('test', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
