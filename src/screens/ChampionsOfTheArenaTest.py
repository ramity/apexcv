import cv2
from ChampionsOfTheArena import ChampionsOfTheArena

image = cv2.imread("../input/scenes/championsOfTheArenaCapture.JPG")

screen = ChampionsOfTheArena()
screen.setImage(image)

print(screen.isInChamptionTeamUI())

screen.drawRegions()
cv2.imwrite("../output/1.jpg", screen.getImage())
