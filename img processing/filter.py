# IG Style Filter app

import cv2
import numpy as np

# dummy function, does nothing
def dummy(value):
    pass

# define convolution kernels
idKernel = np.array([[0,0,0], [0,1,0], [0,0,0]])
sharpKernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
gaussKernel = cv2.getGaussianKernel(3,0)
gaussKernel2 = cv2.getGaussianKernel(15,0)
boxKernel = np.array([[1,1,1], [1,1,1], [1,1,1]], np.float32) / 9

kernels = [idKernel, sharpKernel, gaussKernel, gaussKernel2, boxKernel]

# creating UI (window and trackbars)
cv2.namedWindow('app', cv2.WINDOW_AUTOSIZE)

# read img and make greyscale copy
colorOG = cv2.imread('mke.jpg')
greyOG = cv2.cvtColor(colorOG, cv2.COLOR_BGR2GRAY)

# arguments: trackbarName, windowName, value (initial value), count (max value), onChange (event handler)
cv2.createTrackbar('contrast', 'app', 1, 10, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy)
cv2.createTrackbar('greyscale', 'app', 0, 1, dummy)


# main UI loop
count = 1
while True:
    # read trackbar filters
    greyscale = cv2.getTrackbarPos('greyscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    idxKernel = cv2.getTrackbarPos('filter', 'app')
    
    # TODO: apply filters

    colorMod = cv2.filter2D(colorOG, -1, kernels[idxKernel])
    greyMod = cv2.filter2D(greyOG, -1, kernels[idxKernel])
    
    # TODO: apply brightness/contrast
    colorMod = cv2.addWeighted(colorMod, contrast, np.zeros_like(colorOG), 0, brightness - 50)
    greyMod = cv2.addWeighted(greyMod, contrast, np.zeros_like(greyOG), 0, brightness - 50)
    # wait for keypress
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    elif key == ord('s'):
        if greyscale == 0:
            cv2.imwrite('output_{}.png'.format(count), colorMod)
        else:
            cv2.imwrite('output_{}.png'.format(count), greyMod)
        count += 1

    # show img
    if greyscale == 0:
        # TODO: replace with modified img
        cv2.imshow('app', colorMod)
    else:
        cv2.imshow('app', greyMod)

# window cleanup
cv2.destroyAllWindows()
