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
