import cv2
import numpy as np 
import time

video=cv2.VideoCapture(0)

time.sleep(1)
count=0
background=0

#capturing the image from the background at the staart of the video
for i in range(60):
    return_val,background=video.read()
    if return_val==False:
        continue
background=np.flip(background,axis=1)

while True:
    status,frame=video.read()
    
    if not status:
        print("Cannot access the camera")
        break
    
    count+=1
    
    img=np.flip(frame,axis=1)
    
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    #creating the thresholds
    #hue saturation value
    lower_red=np.array([100,40,40])
    higher_red=np.array([100,255,255])
    
    mask1=cv2.inRange(hsv,lower_red,higher_red)
    
    lower_red=np.array([155,40,40])
    higher_red=np.array([180,255,255])
    
    mask2=cv2.inRange(hsv,lower_red,higher_red)
    
    mask1=mask1+mask2
    
    #Refining image
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
    
    mask2=cv2.bitwise_not(mask1)
    
    #blending the two images together
    
    result1=cv2.bitwise_and(background,background,mask=mask1)
    result2=cv2.bitwise_and(img,img,mask=mask2)

    output=cv2.addWeighted(result1,1,result2,1,0)
    