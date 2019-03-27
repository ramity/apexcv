import numpy as np
import cv2

uiMapX1 = 48
uiMapY1 = 48
uiMapW = 244
uiMapH = 244
uiMapX2 = uiMapX1 + uiMapW
uiMapY2 = uiMapY1 + uiMapH

uiMapCharacterX1 = 112
uiMapCharacterY1 = 109
uiMapCharacterW = 18
uiMapCharacterH = 18
uiMapCharacterX2 = uiMapCharacterX1 + uiMapCharacterW
uiMapCharacterY2 = uiMapCharacterY1 + uiMapCharacterH

uiMapCharacterLower = np.array((110, 128, 15), dtype="uint8")
uiMapCharacterUpper = np.array((182, 194, 74), dtype="uint8")

video = cv2.VideoCapture('./input/footage/1.mp4')

frameCount = 1
while(video.isOpened()):
    # input the frame
    ret, frame = video.read()

    frame[169:171,169:171] = (255, 255, 255)

    # crop out the location of the map
    uiMap = frame[uiMapY1:uiMapY2, uiMapX1:uiMapX2]
    grayUiMap = cv2.cvtColor(uiMap, cv2.COLOR_RGB2GRAY)
    grayUiCharacter = grayUiMap[uiMapCharacterY1:uiMapCharacterY2, uiMapCharacterX1:uiMapCharacterX2]
    #mask = cv2.inRange(uiMap, uiMapCharacterLower, uiMapCharacterUpper)
    #output = cv2.bitwise_and(uiMap, uiMap, mask=mask)

    # process the masked image
    #gray = cv2.cvtColor(output, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(grayUiCharacter, 100, 125, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if(contours):
        contour = sorted(contours, key=cv2.contourArea, reverse=True)[0]
        M = cv2.moments(contour)

        if(M['m00']):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(thresh, (cx, cy), 1, 255, -1)

        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(thresh, [box], 0, (255), 1)


    # write outputMap
    outputFileName = "./output/frame" + str(frameCount) + ".jpg"
    cv2.imwrite(outputFileName, uiMap)
    frameCount += 1

video.release()
