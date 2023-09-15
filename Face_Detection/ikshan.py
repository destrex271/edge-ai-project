import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')


def detect(gray, frame):
    #Detect faces 
    faces = face_cascade.detectMultiScale(gray, 1.3, 3) #1.3 is the scaling factor, and 5 is the number of nearest neighbors
    for (x, y, w, h) in faces:
        # cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        #Detect smiles
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 18)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
        
        #Detect eyes
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), ((ex + ew), (ey + eh)), (0, 255, 0), 2)
    return frame

video_capture = cv2.VideoCapture(0)
while video_capture.isOpened():
    _, frame = video_capture.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
      
    # calls the detect() function    
    canvas = detect(gray, frame)   
    cv2.imshow('Video', canvas) 
  
    if cv2.waitKey(1) & 0xff == ord('q'):               
        break
  
video_capture.release()                                 
cv2.destroyAllWindows()
