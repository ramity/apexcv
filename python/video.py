import cv2
from frame import Frame

class Video:

    videoPath = ""
    framesDirectory = "/var/src/output/frames"
    video
    frameCount = 0
    cols = 0
    rows = 0
    frames = {}

    def __init__(self, videoPath, slowInport=false):
        self.videoPath = videoPath
        self.video = cv2.VideoCapture(videoPath)
        self.frameCount = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.cols = int(self.video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
        self.rows = int(self.video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

        if(slowInport):
            self.loadInFrames()

    def buildFramePath(self, key):
        return framesDirectory + "/" + str(key) + ".jpg"

    def getFrame(self, key):
        frame = frames[key]

        if(frame == None):
            loadInFrame(key):

        return frames[key]

    def loadInFrame(self, key):
        self.video.set(1, key)
        image = video.read()[1]
        framePath = self.buildFramePath(key)
        frames[key] = Frame(z, framePath, image)
        video.set(1, 0)

    def loadInFrames(self, endFrameKey=self.frameCount-1):
        for key in range(endFrameKey):
            image = video.read()[1]
            framePath = self.buildFramePath(key)
            frames[key] = Frame(z, framePath, image)
