import cv2
from inventoryProcessor import InventoryProcessor

image = cv2.imread("../input/ammoCaptures/inv60EnergyAmmoAllowed.JPG")

inventoryProcessor = InventoryProcessor()
inventoryProcessor.setImage(image)

print(inventoryProcessor.isInInventoryUI())

print(inventoryProcessor.isBackpackSlot5Locked())
print(inventoryProcessor.isBackpackSlot6Locked())
print(inventoryProcessor.isBackpackSlot7Locked())

print(inventoryProcessor.isBackpackSlot12Locked())
print(inventoryProcessor.isBackpackSlot13Locked())
print(inventoryProcessor.isBackpackSlot14Locked())

inventoryProcessor.drawRegions()
cv2.imwrite("../output/0.jpg", inventoryProcessor.getImage())
