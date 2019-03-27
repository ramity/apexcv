import cv2
from inventory import Inventory

image = cv2.imread("../input/weaponCaptures/alternator/alternatorSecondaryGame.JPG")

inventoryProcessor = Inventory()
inventoryProcessor.setImage(image)
print(inventoryProcessor.isInInventoryUI())

inventoryProcessor.drawRegions()
cv2.imwrite("../output/0.jpg", inventoryProcessor.getImage())
