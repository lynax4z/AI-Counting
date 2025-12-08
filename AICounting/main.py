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

prev_tick = cv2.getTickCount()
freq = cv2.getTickFrequency()
fps_smooth = 0.0

while True:
    ret, frame = cap.read()
    if not ret:
        print("can't receive the frame")
        break
    current_tick = cv2.getTickCount()
    dt = (current_tick - prev_tick) / freq  # detik
    prev_tick = current_tick
    if dt > 0:
        fps_inst = 1.0 / dt   # FPS instan
        # smoothing: 90% nilai lama, 10% nilai baru
        fps_smooth = fps_inst if fps_smooth == 0 else (0.9 * fps_smooth + 0.1 * fps_inst)
    else:
        fps_inst = 0.0
    boxes = optimize.detect(frame)
    count = len(boxes)
    cv2.putText(frame, f'count : {count}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'FPS : {fps_smooth:.2f}', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('test', frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
