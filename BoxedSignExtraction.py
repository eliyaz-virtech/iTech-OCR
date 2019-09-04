# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:25:50 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:52:22 
2019
@author: user
"""

import cv2 
import math
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from skimage import measure, morphology
from skimage.color import label2rgb
from skimage.measure import regionprops

image = cv2.imread("C:/Users/user/Downloads/signature_extractor-master/inp/in4.jpg")
#img = cv2.imread("C:/Users/user/Downloads/signature_extractor-master/inputs/in9.jpg")

print(image.shape)

print((image.shape[0])//3)
print((image.shape[1])//3)
wt=int(image.shape[1])
ht=int(image.shape[0])
idx=0
bx=0

for i in range(1,9):
    if(i-1==0):
        tl=[0,0]
        br=[wt//2,ht//2]
    elif(i==2):
        tl=[wt//2,0]
        br=[wt,ht//2]
    elif(i==3):
        tl=[0,ht//2]
        br=[wt//2,ht]
    elif(i==4):
        tl=[wt//2,ht//2]
        br=[wt,ht]
    elif(i==5):
        tl=[wt//4,ht//4]
        br=[wt,ht]
    elif(i==6):
        tl=[0,0]
        br=[(3*wt)//4,(3*ht)//4] 
    elif(i==7):
        tl=[wt//4,0]
        br=[(wt),(3*ht)//4]
    elif(i==8):
        tl=[0,ht//4]
        br=[(3*wt)//4,ht]
        

    #tl  = [0, 0]  
    #br = [1174,822]

    rectImg=cv2.rectangle(image,(tl[0],tl[1]),(br[0],br[1]),(0,255,0),3)
    roi = image[tl[1]:br[1], tl[0]:br[0]]
    cv2.imwrite('exp1'+str(i)+'.png',roi)
    
    #distance = math.sqrt( ((tl[0]-br[0])**2)+((tl[1]-br[1])**2) )
    cX = int((tl[0]+br[0])//2)
    cY = int((tl[1] + br[1])//2)

    #cv2.circle(image, (cX, cY), 7, (255, 97, 255), 3)

    cv2.line(image,(cX,cY),(cX,cY),(255,0,0),20)
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(roi, 10, 270)
    (_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    xt1=0
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
    #if (w>62 and w<250) and (h>50 and h<165) and (d>8):
        #xt+=1
        
        if (w<840 and w>700) and (h>250 and h<350):
            print('in else')
            idx+=1
            print('h='+str(h))
            print('w='+str(w))
            print(y)
            print(x)
            img=roi[y:y+h,x:x+w]
            kernel = np.ones((5,5),np.uint8)
            img = cv2.erode(img,kernel,iterations = 1)
            cv2.imwrite(str(idx)+'-'+str(w)+'-'+str(h)+' bx='+str(i)+'.jpg', img)
            
            img = cv2.erode(img,kernel,iterations = 1)
            cimg=roi[y+18:y+h-20,x+18:x+w-20]
            
            cv2.imwrite('final.png',cimg)
            
            img = cv2.imread('final.png', 0)
            print('read')
            img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1] 
            blobs = img > img.mean()
            blobs_labels = measure.label(blobs, background=1)
            image_label_overlay = label2rgb(blobs_labels, image=img)
            fig, ax = plt.subplots(figsize=(10, 6))
            the_biggest_component = 0
            total_area = 0
            counter = 0
            average = 0.0
            for region in regionprops(blobs_labels):
                if (region.area > 10):
                    total_area = total_area + region.area
                    counter = counter + 1
    # print region.area # (for debugging)
    # take regions with large enough areas
                if (region.area >= 250 ):
                    print(region.area)
                    if (region.area > the_biggest_component):
                        the_biggest_component = region.area
            average = (total_area/counter)
            #a4_constant = ((average/150.0)*10.0)+100
            a4_constant = ((average/24.0)*80.0)+100
            b = morphology.remove_small_objects(blobs_labels, a4_constant)
            plt.imsave('pre_version.png', b)
            # read the pre-version
            img = cv2.imread('pre_version.png', 0)
            # ensure binary
            img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            # save the the result
            cv2.imwrite("output.png", img)

    
    
image = cv2.resize(image, (750,600))
cv2.imshow("rectangle",image)
cv2.imwrite('exp'+'.png',image)
cv2.waitKey(0)
cv2.destroyAllWindows()