import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True 
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name = take_snapshot()
main()