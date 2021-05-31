import cv2 
def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        cv2.imwrite("newpicture1.jpg", frame)
        cv2.destroyAllWindows()
        print("Hello")
take_snapshot()        