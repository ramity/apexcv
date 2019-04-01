import cv2
import pytesseract
from difflib import SequenceMatcher

class Base:

    image = None
    regionColor = (0, 0, 255)
    regionThickness = 1

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def getSimilarity(self, stringA, stringB):
        return SequenceMatcher(None, stringA, stringB).ratio()
