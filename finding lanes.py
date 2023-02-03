import cv2
import numpy as np
import matplotlib.pyplot as plt

def avg_lines(img,lines ):
    left=[]
    right=[]
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        m_b = np.polyfit((x1, x2), (y1, y2) , 1)
        m = m_b[0]
        b =m_b[1]
        if m < 0 :
            left.append((m,b))
        else:
            right.append((m,b))
    left_avg = np.average(left, axis=0)
    right_avg = np.average(right, axis=0)
    print(left_avg,'left')
    print(right_avg,'right')
    left_lines = coordinates_of(left_avg,img)
    right_lines = coordinates_of(right_avg,img)
    edges = np.array([left_lines,right_lines])
    return edges

def coordinates_of(lin, img):
    try:
        m,b = lin
        y1 = img.shape[0]
        y2 =int(y1*0.5)
        x1 = int((y1-b)/m)
        x2 = int((y2-b)/m)
        coord =np.array([x1, y1, x2, y2])
    except:
        coord = np.array([0,0,0,0])
    return coord


def masking(img):
    height = img.shape[0]
    width =  img.shape[1]
    region = np.array([[ ( int(width*0.2), height ), ( int(width*0.8), height ),
                         ( int(width*0.6), int(height*0.5) ), ( int(width*0.3), int(height*0.5) ) ]])
    z_img = np.zeros_like(img)
    cv2.fillPoly(z_img,region,255)
    masked_img = cv2.bitwise_and(img,z_img)
    return masked_img

def edg_detection(img,edges):
    if edges is not None:
        for line in edges:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(img,(x1,y1), (x2,y2), (0,255,0), 10)
    return img


def canny(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    canny_img = cv2.Canny(blur_img, 40, 120)
    return canny_img

# img = cv2.imread('test_image.jpg')
# cope_img = np.copy(img)
# canny_img = canny(cope_img)
# masked_img = masking(canny_img)
# lines = cv2.HoughLinesP(masked_img, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
# lin_L_R = avg_lines(cope_img, lines)
# finall = edg_detection(cope_img,lin_L_R)
#
# cv2.imshow('resualts', finall)q
# cv2.waitKey(0)

cap = cv2.VideoCapture("test2.mp4")
while (1):
    _,frame = cap.read()

    canny_img = canny(frame)
    masked_img = masking(canny_img)
    lines = cv2.HoughLinesP(masked_img, 6  , np.pi / 180, 100, np.array([]), minLineLength=10, maxLineGap=5)
    lin_L_R = avg_lines(frame, lines)
    finall = edg_detection(frame, lin_L_R)

    cv2.imshow('resualts', finall)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyWindow('w')