import cv2
import numpy as np 
import time

video=cv2.VideoCapture(0)

time.sleep(1)

count=0
background=0
for i in range(60):
    
    value,bg=video.read()
    if value==False:
        continue
    
bg=np.flip(bg,axis=1)



while True:
    working,frame=video.read()
    if not working:
        print("Error")
        break
    
    count+=1
    
    image=np.flip(frame,axis=1)
    
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
    lower_green=np.array([100,40,40])
    higher_green=np.array([100,255,255])
    
    mask1=cv2.inRange(hsv,lower_green,higher_green)
    
    lower_green=np.array([155,40,40])
    higher_green=np.array([180,255,255])
    
    mask2=cv2.inRange(hsv,lower_green,higher_green)
    
    mask1=mask1+mask2
    
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
    
    mask2=cv2.bitwise_not(mask1)
    
    
    result1=cv2.bitwise_and(background,background,mask=mask1)
    result2=cv2.bitwise_and(image,image,mask=mask2)

    output=cv2.addWeighted(result1,1,result2,1,0)