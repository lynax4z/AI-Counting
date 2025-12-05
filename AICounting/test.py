import cv2 as cv
import time

face_cascade = cv.CascadeClassifier('/Volumes/Macintosh HD/Users/vencent/AICounting/haarcascade_frontalface_alt2.xml')
#eye_cascade = cv.CascadeClassifier('')
#frame_count = 0

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_HEIGHT, 640)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv.CAP_PROP_FPS, 30)

if not cap.isOpened():
	print('there is no camera opened')
	exit()
	
def closeWindow():
	cap.release() #rilis kamera setelah exit biar gak nyala webcam nya dan ga stuck per frame
	cv.destroyAllWindows() #biar ga stuck di window nya (after exit biasanya kalo gapake fungsi tersebut jadi hitam plong)
	exit()
	
def eyeDetection(frame):
	optimized_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #konversi biar deteksi jadi lebih mantep (format opencv BGR bukan RGB)
	eye_rect = eye_cascade.detectMultiScale(optimized_frame, scaleFactor=1.1, minNeighbors=12, minSize=(30, 30)) #isi argumen(frame, scale factor, minNeighbor, size objek)
	return eye_rect
	
def faceDetection(frame):
	optimized_frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY) #sama kaya sebelumnya
	face_rect = face_cascade.detectMultiScale(optimized_frame, scaleFactor=1.1, minNeighbors=12, minSize=(30, 30)) #ini uga
	return face_rect
	
def box(frame):
	for (x, y, w, h) in faceDetection(frame):
	    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=5) #argumen(frame, (titik pojok kiri atas), (titik pojok kanan bawah), (B, G, R), ketebalan warna kotak)
	#for (x, y, w, h) in eyeDetection(frame):
		#cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=5) #sama aja
		
def main():
	while True:
		#global frame_count
		ret, frame = cap.read() #baca frame
		#frame = cv.resize(frame, (340, 240)) #atau ke 640, 620
		#frame_count += 1
		#if frame_count % 3 == 0: -> ngambil per 3 frame
		box(frame)
		if not ret:
			print('cannot receive the frame')
			break
		cv.imshow('test', frame) #display
		if cv.waitKey(27) & 0xFF == ord('q'):
			closeWindow()
			
if __name__ == '__main__':
	main()
