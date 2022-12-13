import cv2
import numpy as np
from rembg import remove
from PIL import Image

#Removing Background
def changeColor(sfilename,tfilename):
    sfilename = 'static/uploads/' + sfilename
    tfilename = 'static/images/' + tfilename
    
    output_path = "static/images/out.png"
    input = Image.open(sfilename)
    output1 = remove(input)
    output1.save(output_path) 

    oimage=cv2.imread(sfilename)
    owidth = oimage.shape[1]
    oheight = oimage.shape[0]
    rimage =cv2.imread(output_path)
    bimage = oimage - rimage
    ## Changing the color of the sofa to the required color

    original_img = cv2.imread('static/images/out.png')
    original_img = cv2.resize(original_img,(720,540))

    target_img= cv2.imread(tfilename)
    target_img = cv2.resize(target_img,(120,60))
    img_hsv = cv2.cvtColor(target_img, cv2.COLOR_BGR2HSV)
    ht,st,vt =cv2.split(img_hsv)

    hsv = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
    center = hsv[hsv.shape[0]//2,hsv.shape[1]//2]
    ho,so,vo = cv2.split(hsv)
    h = center[0]
    h_max=np.max(ho)
    print(h_max)
    print(h)

    for i in range(0,540,60):
        for j in range(0,720,120):
            for row in range(0,60):
                  for col in range(0,120):
                        if (ho[row+i][col+j]>0) or (ho[row+i][col+j]<=h_max):
                                ho[row+i][col+j] = ht[row][col]
                                so[row+i][col+j] = st[row][col]
             
                   
    vo = np.clip(vo + 10, 0, 255)
    hsv = cv2.merge([ho, so, vo])
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imwrite('static/images/foreground.jpg',bgr)
    fimage = cv2.imread('static/images/foreground.jpg')
    fimage = cv2.resize(fimage,(owidth,oheight))
    final_image=bimage + fimage
    cv2.imwrite('static/images/output.jpg',final_image)
    result='output.jpg'
    return(result)

