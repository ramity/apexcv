import os
import numpy as np

class Frame:

    path = ""
    frameNumber = 1
    image
    cols = 0
    rows = 0

    # default configured opencv settings
    simpleBlurAmount = 25
    thresholdType = cv2.THRESH_BINARY
    bilateralKernelSize = 9
    bilateralSigmaSpace = 9
    countourRetrivalMode = cv2.RETR_LIST
    contourApproximationMethod = cv2.CHAIN_APPROX_SIMPLE
    contourLayers = -1
    contourColor = (0, 0, 255)
    contourBorderSize = 1
    floodFillMask

    def __init__(self, frameNumber, path, image):
        self.frameNumber = frameNumber
        self.path = path
        self.image = image
        self.cols = image.shape[0]
        self.rows = image.shape[1]
        self.floodFillMask = np.zeros((self.rows + 2, self.cols + 2), np.unit8)

    def getSubRegion(self, x, y, w, h):
        x1 = x
        x2 = x + w
        y1 = y
        y2 = y + h
        return self.image[y1:y2, x1:x2]

    def getGrayscale(self):
        return cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

    def getGrayscaleSubRegion(self, x, y, w, h):
        x1 = x
        x2 = x + w
        y1 = y
        y2 = y + h
        image = self.image[y1:y2, x1:x2]
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    def getSimpleBlur(self):
        kernel = np.ones((5, 5), np.float32) / self.simpleBlurAmount
        return cv2.filter2D(self.image, -1, kernel)

    def getSimpleBlurSubRegion(self, x, y, w, h):
        x1 = x
        x2 = x + w
        y1 = y
        y2 = y + h
        image = self.image[y1:y2, x1:x2]
        kernel = np.ones((5, 5), np.float32) / self.simpleBlurAmount
        return cv2.filter2D(image, -1, kernel)

    def getThreshold(self, low, high):
        return cv2.threshold(self.image, low, high, self.thresholdType)

    def getThresholdSubRegion(self, low, high, x, y, w, h):
        x1 = x
        x2 = x + w
        y1 = y
        y2 = y + h
        image = self.image[y1:y2, x1:x2]
        return cv2.GaussianBlur(image, (5,5), 0)

    def getBilateral(self):
        return cv2.adaptiveBilateralFilter(self.image, self.bilateralKernelSize, self.bilateralSigmaSpace)

    def getBilateralSubRegion(self, x, y, w, h):
        x1 = x
        x2 = x + w
        y1 = y
        y2 = y + h
        image = self.image[y1:y2, x1:x2]
        return cv2.adaptiveBilateralFilter(image, self.bilateralKernelSize, self.bilateralSigmaSpace)

    def getContours(self):
        gray = self.getGrayscale()
        return cv2.findContours(gray, self.countourRetrivalMode, self.contourApproximationMethod)

    def getContoursOverlayImage(self):
        contours = self.getContours()

        if(contours == None):
            return self.image
        else:
            return cv2.drawContours(self.image, contours, self.contourLayers, self.contourColor, self.contourBorderSize)

    def getContoursSubRegion(self, x, y, w, h):
        gray = self.getGrayscaleSubRegion(x, y, w, h)
        return cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    def getContoursOverlayImage(self, x, y, w, h):
        contours = self.getContoursSubRegion(x, y, w, h)

        if(contours == None):
            return self.getSubRegion(x, y, w, h)
        else:
            return cv2.drawContours(self.getSubRegion(x, y, w, h), contours, self.contourLayers, self.contourColor, self.contourBorderSize)

    def floodFill(self, x, y):
        return cv2.floodFill(self.getGrayscale(), self.floodFillMask, (x, y), self.floodFillColor)
