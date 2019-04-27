import cv2
from Inventory import Inventory

image = cv2.imread("../input/scenes/emptyInventoryDamagedTrainingArea.jpg")
#image = cv2.imread("../input/scenes/populatedInventory1.jpg")

screen = Inventory()
screen.setImage(image)

print(screen.isInInventoryUI())

print(screen.isBackpackSlot5Locked())
print(screen.isBackpackSlot6Locked())
print(screen.isBackpackSlot7Locked())

print(screen.isBackpackSlot12Locked())
print(screen.isBackpackSlot13Locked())
print(screen.isBackpackSlot14Locked())

print(screen.getHealthAmount())

screen.drawRegions()
cv2.imwrite("../output/0.jpg", screen.getImage())
