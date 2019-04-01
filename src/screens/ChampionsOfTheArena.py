import cv2
import pytesseract
from Base import Base

class ChampionsOfTheArena(Base):

    confidenceLevelRequirement = 2
    confidenceLevelOutput = True

    championsOfTheArenaTextX1 = 583
    championsOfTheArenaTextW = 758
    championsOfTheArenaTextY1 = 54
    championsOfTheArenaTextH = 44

    placedTextX1 = 609
    placedTextW = 87
    placedTextY1 = 133
    placedTextH = 22

    ofTextX1 = 609
    ofTextW = 87
    ofTextY1 = 133
    ofTextH = 22

    fullPlacedTextX1 = 609
    fullPlacedTextW = 187
    fullPlacedTextY1 = 128
    fullPlacedTextH = 27

    # player 1

    player1UsernameX1 = 216
    player1UsernameW = 264
    player1UsernameY1 = 179
    player1UsernameH = 28

    player1Tracker1NameX1 = 138
    player1Tracker1NameW = 193
    player1Tracker1NameY1 = 633
    player1Tracker1NameH = 20

    player1Tracker1ValueX1 = 138
    player1Tracker1ValueW = 193
    player1Tracker1ValueY1 = 653
    player1Tracker1ValueH = 41

    player1Tracker2NameX1 = 138
    player1Tracker2NameW = 193
    player1Tracker2NameY1 = 706
    player1Tracker2NameH = 20

    player1Tracker2ValueX1 = 138
    player1Tracker2ValueW = 193
    player1Tracker2ValueY1 = 726
    player1Tracker2ValueH = 41

    player1Tracker3NameX1 = 138
    player1Tracker3NameW = 193
    player1Tracker3NameY1 = 779
    player1Tracker3NameH = 20

    player1Tracker3ValueX1 = 138
    player1Tracker3ValueW = 193
    player1Tracker3ValueY1 = 799
    player1Tracker3ValueH = 41

    player1Tracker4NameX1 = 138
    player1Tracker4NameW = 193
    player1Tracker4NameY1 = 852
    player1Tracker4NameH = 20

    player1Tracker4ValueX1 = 138
    player1Tracker4ValueW = 193
    player1Tracker4ValueY1 = 872
    player1Tracker4ValueH = 41

    player1Tracker5NameX1 = 138
    player1Tracker5NameW = 193
    player1Tracker5NameY1 = 925
    player1Tracker5NameH = 20

    player1Tracker5ValueX1 = 138
    player1Tracker5ValueW = 193
    player1Tracker5ValueY1 = 945
    player1Tracker5ValueH = 41

    # player 2

    player2UsernameX1 = 829
    player2UsernameW = 264
    player2UsernameY1 = 179
    player2UsernameH = 28

    player2Tracker1NameX1 = 763
    player2Tracker1NameW = 193
    player2Tracker1NameY1 = 633
    player2Tracker1NameH = 20

    player2Tracker1ValueX1 = 763
    player2Tracker1ValueW = 193
    player2Tracker1ValueY1 = 653
    player2Tracker1ValueH = 41

    player2Tracker2NameX1 = 763
    player2Tracker2NameW = 193
    player2Tracker2NameY1 = 706
    player2Tracker2NameH = 20

    player2Tracker2ValueX1 = 763
    player2Tracker2ValueW = 193
    player2Tracker2ValueY1 = 726
    player2Tracker2ValueH = 41

    player2Tracker3NameX1 = 763
    player2Tracker3NameW = 193
    player2Tracker3NameY1 = 779
    player2Tracker3NameH = 20

    player2Tracker3ValueX1 = 763
    player2Tracker3ValueW = 193
    player2Tracker3ValueY1 = 799
    player2Tracker3ValueH = 41

    player2Tracker4NameX1 = 763
    player2Tracker4NameW = 193
    player2Tracker4NameY1 = 852
    player2Tracker4NameH = 20

    player2Tracker4ValueX1 = 763
    player2Tracker4ValueW = 193
    player2Tracker4ValueY1 = 872
    player2Tracker4ValueH = 41

    player2Tracker5NameX1 = 763
    player2Tracker5NameW = 193
    player2Tracker5NameY1 = 925
    player2Tracker5NameH = 20

    player2Tracker5ValueX1 = 763
    player2Tracker5ValueW = 193
    player2Tracker5ValueY1 = 945
    player2Tracker5ValueH = 41

    # player 3

    player3UsernameX1 = 1440
    player3UsernameW = 264
    player3UsernameY1 = 179
    player3UsernameH = 28

    player3Tracker1NameX1 = 1388
    player3Tracker1NameW = 193
    player3Tracker1NameY1 = 633
    player3Tracker1NameH = 20

    player3Tracker1ValueX1 = 1388
    player3Tracker1ValueW = 193
    player3Tracker1ValueY1 = 653
    player3Tracker1ValueH = 41

    player3Tracker2NameX1 = 1388
    player3Tracker2NameW = 193
    player3Tracker2NameY1 = 706
    player3Tracker2NameH = 20

    player3Tracker2ValueX1 = 1388
    player3Tracker2ValueW = 193
    player3Tracker2ValueY1 = 726
    player3Tracker2ValueH = 41

    player3Tracker3NameX1 = 1388
    player3Tracker3NameW = 193
    player3Tracker3NameY1 = 779
    player3Tracker3NameH = 20

    player3Tracker3ValueX1 = 1388
    player3Tracker3ValueW = 193
    player3Tracker3ValueY1 = 799
    player3Tracker3ValueH = 41

    player3Tracker4NameX1 = 1388
    player3Tracker4NameW = 193
    player3Tracker4NameY1 = 852
    player3Tracker4NameH = 20

    player3Tracker4ValueX1 = 1388
    player3Tracker4ValueW = 193
    player3Tracker4ValueY1 = 872
    player3Tracker4ValueH = 41

    player3Tracker5NameX1 = 1388
    player3Tracker5NameW = 193
    player3Tracker5NameY1 = 925
    player3Tracker5NameH = 20

    player3Tracker5ValueX1 = 1388
    player3Tracker5ValueW = 193
    player3Tracker5ValueY1 = 945
    player3Tracker5ValueH = 41

    returnToLobbyTextX1 = 1679
    returnToLobbyTextW = 195
    returnToLobbyTextY1 = 1027
    returnToLobbyTextH = 23

    def drawRegions(self):
        self.drawRegionChampionsOfTheArenaText()
        self.drawRegionPlacedText()
        self.drawRegionOfText()
        self.drawRegionFullPlacedText()
        self.drawRegionPlayer1Username()
        self.drawRegionPlayer1Tracker1Name()
        self.drawRegionPlayer1Tracker1Value()
        self.drawRegionPlayer1Tracker2Name()
        self.drawRegionPlayer1Tracker2Value()
        self.drawRegionPlayer1Tracker3Name()
        self.drawRegionPlayer1Tracker3Value()
        self.drawRegionPlayer1Tracker4Name()
        self.drawRegionPlayer1Tracker4Value()
        self.drawRegionPlayer1Tracker5Name()
        self.drawRegionPlayer1Tracker5Value()

        self.drawRegionPlayer2Username()
        self.drawRegionPlayer2Tracker1Name()
        self.drawRegionPlayer2Tracker1Value()
        self.drawRegionPlayer2Tracker2Name()
        self.drawRegionPlayer2Tracker2Value()
        self.drawRegionPlayer2Tracker3Name()
        self.drawRegionPlayer2Tracker3Value()
        self.drawRegionPlayer2Tracker4Name()
        self.drawRegionPlayer2Tracker4Value()
        self.drawRegionPlayer2Tracker5Name()
        self.drawRegionPlayer2Tracker5Value()

        self.drawRegionPlayer3Username()
        self.drawRegionPlayer3Tracker1Name()
        self.drawRegionPlayer3Tracker1Value()
        self.drawRegionPlayer3Tracker2Name()
        self.drawRegionPlayer3Tracker2Value()
        self.drawRegionPlayer3Tracker3Name()
        self.drawRegionPlayer3Tracker3Value()
        self.drawRegionPlayer3Tracker4Name()
        self.drawRegionPlayer3Tracker4Value()
        self.drawRegionPlayer3Tracker5Name()
        self.drawRegionPlayer3Tracker5Value()

        self.drawRegionReturnToLobby()

    def drawRegionChampionsOfTheArenaText(self):
        pointA = (self.championsOfTheArenaTextX1, self.championsOfTheArenaTextY1)
        pointB = (pointA[0] + self.championsOfTheArenaTextW, pointA[1] + self.championsOfTheArenaTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlacedText(self):
        pointA = (self.placedTextX1, self.placedTextY1)
        pointB = (pointA[0] + self.placedTextW, pointA[1] + self.placedTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionOfText(self):
        pointA = (self.ofTextX1, self.ofTextY1)
        pointB = (pointA[0] + self.ofTextW, pointA[1] + self.ofTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionFullPlacedText(self):
        pointA = (self.fullPlacedTextX1, self.fullPlacedTextY1)
        pointB = (pointA[0] + self.fullPlacedTextW, pointA[1] + self.fullPlacedTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Username(self):
        pointA = (self.player1UsernameX1, self.player1UsernameY1)
        pointB = (pointA[0] + self.player1UsernameW, pointA[1] + self.player1UsernameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker1Name(self):
        pointA = (self.player1Tracker1NameX1, self.player1Tracker1NameY1)
        pointB = (pointA[0] + self.player1Tracker1NameW, pointA[1] + self.player1Tracker1NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker1Value(self):
        pointA = (self.player1Tracker1ValueX1, self.player1Tracker1ValueY1)
        pointB = (pointA[0] + self.player1Tracker1ValueW, pointA[1] + self.player1Tracker1ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker2Name(self):
        pointA = (self.player1Tracker2NameX1, self.player1Tracker2NameY1)
        pointB = (pointA[0] + self.player1Tracker2NameW, pointA[1] + self.player1Tracker2NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker2Value(self):
        pointA = (self.player1Tracker2ValueX1, self.player1Tracker2ValueY1)
        pointB = (pointA[0] + self.player1Tracker2ValueW, pointA[1] + self.player1Tracker2ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker3Name(self):
        pointA = (self.player1Tracker3NameX1, self.player1Tracker3NameY1)
        pointB = (pointA[0] + self.player1Tracker3NameW, pointA[1] + self.player1Tracker3NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker3Value(self):
        pointA = (self.player1Tracker3ValueX1, self.player1Tracker3ValueY1)
        pointB = (pointA[0] + self.player1Tracker3ValueW, pointA[1] + self.player1Tracker3ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker4Name(self):
        pointA = (self.player1Tracker4NameX1, self.player1Tracker4NameY1)
        pointB = (pointA[0] + self.player1Tracker4NameW, pointA[1] + self.player1Tracker4NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker4Value(self):
        pointA = (self.player1Tracker4ValueX1, self.player1Tracker4ValueY1)
        pointB = (pointA[0] + self.player1Tracker4ValueW, pointA[1] + self.player1Tracker4ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker5Name(self):
        pointA = (self.player1Tracker5NameX1, self.player1Tracker5NameY1)
        pointB = (pointA[0] + self.player1Tracker5NameW, pointA[1] + self.player1Tracker5NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer1Tracker5Value(self):
        pointA = (self.player1Tracker5ValueX1, self.player1Tracker5ValueY1)
        pointB = (pointA[0] + self.player1Tracker5ValueW, pointA[1] + self.player1Tracker5ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Username(self):
        pointA = (self.player2UsernameX1, self.player2UsernameY1)
        pointB = (pointA[0] + self.player2UsernameW, pointA[1] + self.player2UsernameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker1Name(self):
        pointA = (self.player2Tracker1NameX1, self.player2Tracker1NameY1)
        pointB = (pointA[0] + self.player2Tracker1NameW, pointA[1] + self.player2Tracker1NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker1Value(self):
        pointA = (self.player2Tracker1ValueX1, self.player2Tracker1ValueY1)
        pointB = (pointA[0] + self.player2Tracker1ValueW, pointA[1] + self.player2Tracker1ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker2Name(self):
        pointA = (self.player2Tracker2NameX1, self.player2Tracker2NameY1)
        pointB = (pointA[0] + self.player2Tracker2NameW, pointA[1] + self.player2Tracker2NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker2Value(self):
        pointA = (self.player2Tracker2ValueX1, self.player2Tracker2ValueY1)
        pointB = (pointA[0] + self.player2Tracker2ValueW, pointA[1] + self.player2Tracker2ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker3Name(self):
        pointA = (self.player2Tracker3NameX1, self.player2Tracker3NameY1)
        pointB = (pointA[0] + self.player2Tracker3NameW, pointA[1] + self.player2Tracker3NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker3Value(self):
        pointA = (self.player2Tracker3ValueX1, self.player2Tracker3ValueY1)
        pointB = (pointA[0] + self.player2Tracker3ValueW, pointA[1] + self.player2Tracker3ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker4Name(self):
        pointA = (self.player2Tracker4NameX1, self.player2Tracker4NameY1)
        pointB = (pointA[0] + self.player2Tracker4NameW, pointA[1] + self.player2Tracker4NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker4Value(self):
        pointA = (self.player2Tracker4ValueX1, self.player2Tracker4ValueY1)
        pointB = (pointA[0] + self.player2Tracker4ValueW, pointA[1] + self.player2Tracker4ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker5Name(self):
        pointA = (self.player2Tracker5NameX1, self.player2Tracker5NameY1)
        pointB = (pointA[0] + self.player2Tracker5NameW, pointA[1] + self.player2Tracker5NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer2Tracker5Value(self):
        pointA = (self.player2Tracker5ValueX1, self.player2Tracker5ValueY1)
        pointB = (pointA[0] + self.player2Tracker5ValueW, pointA[1] + self.player2Tracker5ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Username(self):
        pointA = (self.player3UsernameX1, self.player3UsernameY1)
        pointB = (pointA[0] + self.player3UsernameW, pointA[1] + self.player3UsernameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker1Name(self):
        pointA = (self.player3Tracker1NameX1, self.player3Tracker1NameY1)
        pointB = (pointA[0] + self.player3Tracker1NameW, pointA[1] + self.player3Tracker1NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker1Value(self):
        pointA = (self.player3Tracker1ValueX1, self.player3Tracker1ValueY1)
        pointB = (pointA[0] + self.player3Tracker1ValueW, pointA[1] + self.player3Tracker1ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker2Name(self):
        pointA = (self.player3Tracker2NameX1, self.player3Tracker2NameY1)
        pointB = (pointA[0] + self.player3Tracker2NameW, pointA[1] + self.player3Tracker2NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker2Value(self):
        pointA = (self.player3Tracker2ValueX1, self.player3Tracker2ValueY1)
        pointB = (pointA[0] + self.player3Tracker2ValueW, pointA[1] + self.player3Tracker2ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker3Name(self):
        pointA = (self.player3Tracker3NameX1, self.player3Tracker3NameY1)
        pointB = (pointA[0] + self.player3Tracker3NameW, pointA[1] + self.player3Tracker3NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker3Value(self):
        pointA = (self.player3Tracker3ValueX1, self.player3Tracker3ValueY1)
        pointB = (pointA[0] + self.player3Tracker3ValueW, pointA[1] + self.player3Tracker3ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker4Name(self):
        pointA = (self.player3Tracker4NameX1, self.player3Tracker4NameY1)
        pointB = (pointA[0] + self.player3Tracker4NameW, pointA[1] + self.player3Tracker4NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker4Value(self):
        pointA = (self.player3Tracker4ValueX1, self.player3Tracker4ValueY1)
        pointB = (pointA[0] + self.player3Tracker4ValueW, pointA[1] + self.player3Tracker4ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker5Name(self):
        pointA = (self.player3Tracker5NameX1, self.player3Tracker5NameY1)
        pointB = (pointA[0] + self.player3Tracker5NameW, pointA[1] + self.player3Tracker5NameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionPlayer3Tracker5Value(self):
        pointA = (self.player3Tracker5ValueX1, self.player3Tracker5ValueY1)
        pointB = (pointA[0] + self.player3Tracker5ValueW, pointA[1] + self.player3Tracker5ValueH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionReturnToLobby(self):
        pointA = (self.returnToLobbyTextX1, self.returnToLobbyTextY1)
        pointB = (pointA[0] + self.returnToLobbyTextW, pointA[1] + self.returnToLobbyTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def getChampionsOfTheArenaTextSimilarity(self):
        pointA = (self.championsOfTheArenaTextX1, self.championsOfTheArenaTextY1)
        pointB = (pointA[0] + self.championsOfTheArenaTextW, pointA[1] + self.championsOfTheArenaTextH)

        subImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedText = str(pytesseract.image_to_string(subImage)).lower()
        return self.getSimilarity(processedText, "champions of the arena")

    def getReturnToLobbyTextSimilarity(self):
        pointA = (self.returnToLobbyTextX1, self.returnToLobbyTextY1)
        pointB = (pointA[0] + self.returnToLobbyTextW, pointA[1] + self.returnToLobbyTextH)

        subImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedText = str(pytesseract.image_to_string(subImage)).lower()
        return self.getSimilarity(processedText, "return to lobby")

    def isInChamptionTeamUI(self):
        confidenceLevel = 0

        championsOfTheArenaTextSimilarity = self.getChampionsOfTheArenaTextSimilarity()
        returnToLobbyTextSimilarity = self.getReturnToLobbyTextSimilarity()

        if(championsOfTheArenaTextSimilarity >= .80):
            confidenceLevel += 1
        if(returnToLobbyTextSimilarity >= .80):
            confidenceLevel += 1

        if(self.confidenceLevelOutput):
            print("confidenceLevel: ", confidenceLevel)
            print("confidenceLevelRequirement: ", self.confidenceLevelRequirement)
            print("championsOfTheArenaTextSimilarity: ", championsOfTheArenaTextSimilarity)
            print("returnToLobbyTextSimilarity: ", returnToLobbyTextSimilarity)

        return True if confidenceLevel >= self.confidenceLevelRequirement else False
