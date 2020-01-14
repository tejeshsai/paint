import cv2
import numpy as np

drawing = False 
mode = True 
ix,iy = -1,-1
sizeParameter = 0

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,sizeParameter
    global r,g,b
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(x-sizeParameter,y-sizeParameter),(x+sizeParameter,y+sizeParameter),(b,g,r),-1)
            else:
                cv2.circle(img,(x,y),sizeParameter,(b,g,r),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(x-sizeParameter,y-sizeParameter),(x+sizeParameter,y+sizeParameter),(b,g,r),-1)
        else:
            cv2.circle(img,(x,y),sizeParameter,(b,g,r),-1)
    

def nothing(x):
    pass

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')


cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('SIZE','image',0,100,nothing)
cv2.setMouseCallback('image',draw_circle)
while(1):
    
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    
    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    sizeParameter=cv2.getTrackbarPos('SIZE','image')

cv2.destroyAllWindows()