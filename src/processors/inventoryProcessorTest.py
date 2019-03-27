import cv2
from inventoryProcessor import InventoryProcessor

image = cv2.imread("../input/weaponCaptures/peacekeeper/peacekeeperSecondaryInv.JPG")

inventoryProcessor = InventoryProcessor()
inventoryProcessor.setImage(image)
print(inventoryProcessor.isInInventoryUI())

inventoryProcessor.drawRegions()
cv2.imwrite("../output/0.jpg", inventoryProcessor.getImage())
