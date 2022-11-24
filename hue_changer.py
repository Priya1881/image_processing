import cv2
import numpy as np
import os

def colorChanger(sfilename,tfilename):

    sfilename = 'static/uploads/' + sfilename
    tfilename = 'static/images/' + tfilename

    original_img = cv2.imread(sfilename)
    original_img = cv2.resize(original_img,(600,300))
    
    target_img= cv2.imread(tfilename)
    target_img = cv2.resize(target_img,(150,100))
    
    img_hsv = cv2.cvtColor(target_img, cv2.COLOR_BGR2HSV)
    ht,st,vt =cv2.split(img_hsv)

    hsv = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
    center = hsv[hsv.shape[0]//2,hsv.shape[1]//2]
    h = center[0]
    lower = np.array([h - 10, 50, 20])
    upper = np.array([h + 10, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    inv_mask = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(original_img,original_img,mask=mask)
    sofa_hsv=cv2.cvtColor(res,cv2.COLOR_BGR2HSV)
    ho,so,vo = cv2.split(sofa_hsv)

    for i in range(0,300,100):
        for j in range(0,600,150):
            for row in range(0,100):
                for col in range(0,150):
                    if (ho[row+i][col+j] > h-10 and ho[row+i][col+j]< h+10):
                            ho[row+i][col+j] = ht[row][col]
                            so[row+i][col+j] = st[row][col]
                   
    vo = np.clip(vo + 40, 0, 255)
    hsv = cv2.merge([ho, so, vo])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    result = cv2.bitwise_or(cv2.bitwise_and(original_img, original_img, mask=inv_mask), cv2.bitwise_and(bgr, bgr, mask=mask))
    path='static/images/'
    cv2.imwrite(os.path.join(path, 'output.jpg'), result)  
    result='output.jpg'
    return (result)


   


