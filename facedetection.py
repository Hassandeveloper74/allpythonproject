import cv2

# video_cap=cv2.VideoCapture(0)
# while True :
#     ret,vid=video_cap.read()
#     cv2.imshow("video_live",vid)
#     if cv2.waitKey(10) == ord("a"):                 this code is only camera open 
#         break

# video_cap.release()

face_cap=cv2.CascadeClassifier("C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
video_cap=cv2.VideoCapture(0)
while True :
    ret,vid=video_cap.read()
    col=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    face=face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    for x,y,w,h in face:
        cv2.rectangle(vid,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("video_live",vid)
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()