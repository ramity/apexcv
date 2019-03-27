import cv2
from inventoryProcessor import InventoryProcessor

image = cv2.imread("../input/weaponCaptures/alternator/alternatorSecondaryGame.JPG")

inventoryProcessor = InventoryProcessor()
inventoryProcessor.setImage(image)
print(inventoryProcessor.isInInventoryUI())

inventoryProcessor.drawRegions()
cv2.imwrite("../output/0.jpg", inventoryProcessor.getImage())
