import cv2
import pytesseract
from difflib import SequenceMatcher

class InventoryProcessor:

    image = None
    regionColor = (0, 0, 255)
    regionThickness = 1

    topMenuInventoryTextX1 = 704
    topMenuInventoryTextW = 123
    topMenuInventoryTextY1 = 37
    topMenuInventoryTextH = 26

    topMenuSquadTextX1 = 930
    topMenuSquadTextW = 77
    topMenuSquadTextY1 = 37
    topMenuSquadTextH = 26

    topMenuLengendTextX1 = 1129
    topMenuLengendTextW = 88
    topMenuLengendTextY1 = 37
    topMenuLengendTextH = 26

    weapon1BoundingBoxX1 = 410
    weapon1BoundingBoxW = 510
    weapon1BoundingBoxY1 = 150
    weapon1BoundingBoxH = 310

    weapon1KeyBindIconX1 = 424
    weapon1KeyBindIconW = 25
    weapon1KeyBindIconY1 = 155
    weapon1KeyBindIconH = 25

    weapon1TextX1 = 451
    weapon1TextW = 88
    weapon1TextY1 = 156
    weapon1TextH = 21

    weapon1WeaponIconX1 = 536
    weapon1WeaponIconW = 309
    weapon1WeaponIconY1 = 205
    weapon1WeaponIconH = 72

    weapon1WeaponNameX1 = 419
    weapon1WeaponNameW = 299
    weapon1WeaponNameY1 = 315
    weapon1WeaponNameH = 24

    weapon1SkinNameX1 = 421
    weapon1SkinNameW = 150
    weapon1SkinNameY1 = 342
    weapon1SkinNameH = 19

    weapon1ModSlot1X1 = 418
    weapon1ModSlot1W = 75
    weapon1ModSlot1Y1 = 377
    weapon1ModSlot1H = 75

    weapon1ModSlot2X1 = 497
    weapon1ModSlot2W = 75
    weapon1ModSlot2Y1 = 377
    weapon1ModSlot2H = 75

    weapon1ModSlot3X1 = 576
    weapon1ModSlot3W = 75
    weapon1ModSlot3Y1 = 377
    weapon1ModSlot3H = 75

    weapon1ModSlot4X1 = 655
    weapon1ModSlot4W = 75
    weapon1ModSlot4Y1 = 377
    weapon1ModSlot4H = 75

    weapon1ModSlot5X1 = 734
    weapon1ModSlot5W = 75
    weapon1ModSlot5Y1 = 377
    weapon1ModSlot5H = 75

    weapon1CurrentMagizineCountX1 = 848
    weapon1CurrentMagizineCountW = 46
    weapon1CurrentMagizineCountY1 = 334
    weapon1CurrentMagizineCountH = 34

    weapon1AmmoTypeIconX1 = 830
    weapon1AmmoTypeIconW = 83
    weapon1AmmoTypeIconY1 = 372
    weapon1AmmoTypeIconH = 82

    weapon2BoundingBoxX1 = 1000
    weapon2BoundingBoxW = 510
    weapon2BoundingBoxY1 = 150
    weapon2BoundingBoxH = 310

    weapon2KeyBindIconX1 = 1014
    weapon2KeyBindIconW = 25
    weapon2KeyBindIconY1 = 155
    weapon2KeyBindIconH = 25

    weapon2TextX1 = 1041
    weapon2TextW = 88
    weapon2TextY1 = 156
    weapon2TextH = 21

    weapon2WeaponIconX1 = 1126
    weapon2WeaponIconW = 309
    weapon2WeaponIconY1 = 205
    weapon2WeaponIconH = 72

    weapon2WeaponNameX1 = 1009
    weapon2WeaponNameW = 299
    weapon2WeaponNameY1 = 315
    weapon2WeaponNameH = 24

    weapon2SkinNameX1 = 1011
    weapon2SkinNameW = 150
    weapon2SkinNameY1 = 342
    weapon2SkinNameH = 19

    weapon2ModSlot1X1 = 1008
    weapon2ModSlot1W = 75
    weapon2ModSlot1Y1 = 377
    weapon2ModSlot1H = 75

    weapon2ModSlot2X1 = 1087
    weapon2ModSlot2W = 75
    weapon2ModSlot2Y1 = 377
    weapon2ModSlot2H = 75

    weapon2ModSlot3X1 = 1166
    weapon2ModSlot3W = 75
    weapon2ModSlot3Y1 = 377
    weapon2ModSlot3H = 75

    weapon2ModSlot4X1 = 1245
    weapon2ModSlot4W = 75
    weapon2ModSlot4Y1 = 377
    weapon2ModSlot4H = 75

    weapon2ModSlot5X1 = 1324
    weapon2ModSlot5W = 75
    weapon2ModSlot5Y1 = 377
    weapon2ModSlot5H = 75

    weapon2CurrentMagizineCountX1 = 1438
    weapon2CurrentMagizineCountW = 46
    weapon2CurrentMagizineCountY1 = 334
    weapon2CurrentMagizineCountH = 34

    weapon2AmmoTypeIconX1 = 1420
    weapon2AmmoTypeIconW = 83
    weapon2AmmoTypeIconY1 = 372
    weapon2AmmoTypeIconH = 82

    backpackSlot1X1 = 614
    backpackSlot1W = 92
    backpackSlot1Y1 = 590
    backpackSlot1H = 92

    backpackSlot2X1 = 714
    backpackSlot2W = 92
    backpackSlot2Y1 = 590
    backpackSlot2H = 92

    backpackSlot3X1 = 814
    backpackSlot3W = 92
    backpackSlot3Y1 = 590
    backpackSlot3H = 92

    backpackSlot4X1 = 914
    backpackSlot4W = 92
    backpackSlot4Y1 = 590
    backpackSlot4H = 92

    backpackSlot5X1 = 1014
    backpackSlot5W = 92
    backpackSlot5Y1 = 590
    backpackSlot5H = 92

    backpackSlot6X1 = 1114
    backpackSlot6W = 92
    backpackSlot6Y1 = 590
    backpackSlot6H = 92

    backpackSlot7X1 = 1214
    backpackSlot7W = 92
    backpackSlot7Y1 = 590
    backpackSlot7H = 92

    backpackSlot8X1 = 614
    backpackSlot8W = 92
    backpackSlot8Y1 = 690
    backpackSlot8H = 92

    backpackSlot9X1 = 714
    backpackSlot9W = 92
    backpackSlot9Y1 = 690
    backpackSlot9H = 92

    backpackSlot10X1 = 814
    backpackSlot10W = 92
    backpackSlot10Y1 = 690
    backpackSlot10H = 92

    backpackSlot11X1 = 914
    backpackSlot11W = 92
    backpackSlot11Y1 = 690
    backpackSlot11H = 92

    backpackSlot12X1 = 1014
    backpackSlot12W = 92
    backpackSlot12Y1 = 690
    backpackSlot12H = 92

    backpackSlot13X1 = 1114
    backpackSlot13W = 92
    backpackSlot13Y1 = 690
    backpackSlot13H = 92

    backpackSlot14X1 = 1214
    backpackSlot14W = 92
    backpackSlot14Y1 = 690
    backpackSlot14H = 92

    bannerBoundingBoxX1 = 45
    bannerBoundingBoxW = 470
    bannerBoundingBoxY1 = 835
    bannerBoundingBoxH = 97

    legendIconX1 = 89
    legendIconW = 95
    legendIconY1 = 840
    legendIconH = 86

    usernameX1 = 198
    usernameW = 121
    usernameY1 = 853
    usernameH = 26

    healthBarX1 = 199
    healthBarW = 240
    healthBarY1 = 905
    healthBarH = 12

    helmetSlotX1 = 760
    helmetSlotW = 94
    helmetSlotY1 = 835
    helmetSlotH = 94

    armorSlotX1 = 862
    armorSlotW = 94
    armorSlotY1 = 835
    armorSlotH = 94

    knockdownShieldSlotX1 = 964
    knockdownShieldSlotW = 94
    knockdownShieldSlotY1 = 835
    knockdownShieldSlotH = 94

    backpackSlotX1 = 1066
    backpackSlotW = 94
    backpackSlotY1 = 835
    backpackSlotH = 94

    abilityIconX1 = 1383
    abilityIconW = 184
    abilityIconY1 = 780
    abilityIconH = 154

    backButtonKeyBindX1 = 62
    backButtonKeyBindW = 48
    backButtonKeyBindY1 = 1034
    backButtonKeyBindH = 30

    backButtonTextX1 = 113
    backButtonTextW = 52
    backButtonTextY1 = 1037
    backButtonTextH = 22

    gameMenuTextX1 = 1741
    gameMenuTextW = 118
    gameMenuTextY1 = 1037
    gameMenuTextH = 22

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def drawRegions(self):
        self.drawRegionTopMenuInventoryText()
        self.drawRegionTopMenuSquadText()
        self.drawRegionTopMenuLegendText()
        self.drawRegionWeapon1BoundingBox()
        self.drawRegionWeapon1KeyBindIcon()
        self.drawRegionWeapon1Text()
        self.drawRegionWeapon1WeaponName()
        self.drawRegionWeapon1SkinName()
        self.drawRegionWeapon1ModSlot1()
        self.drawRegionWeapon1ModSlot2()
        self.drawRegionWeapon1ModSlot3()
        self.drawRegionWeapon1ModSlot4()
        self.drawRegionWeapon1ModSlot5()
        self.drawRegionWeapon1CurrentMagizineCount()
        self.drawRegionWeapon1AmmoTypeIcon()
        self.drawRegionWeapon2BoundingBox()
        self.drawRegionWeapon2KeyBindIcon()
        self.drawRegionWeapon2Text()
        self.drawRegionWeapon2WeaponIcon()
        self.drawRegionWeapon2WeaponName()
        self.drawRegionWeapon2SkinName()
        self.drawRegionWeapon2ModSlot1()
        self.drawRegionWeapon2ModSlot2()
        self.drawRegionWeapon2ModSlot3()
        self.drawRegionWeapon2ModSlot4()
        self.drawRegionWeapon2ModSlot5()
        self.drawRegionWeapon2CurrentMagizineCount()
        self.drawRegionWeapon2AmmoTypeIcon()
        self.drawRegionBackpackSlot1()
        self.drawRegionBackpackSlot2()
        self.drawRegionBackpackSlot3()
        self.drawRegionBackpackSlot4()
        self.drawRegionBackpackSlot5()
        self.drawRegionBackpackSlot6()
        self.drawRegionBackpackSlot7()
        self.drawRegionBackpackSlot8()
        self.drawRegionBackpackSlot9()
        self.drawRegionBackpackSlot10()
        self.drawRegionBackpackSlot11()
        self.drawRegionBackpackSlot12()
        self.drawRegionBackpackSlot13()
        self.drawRegionBackpackSlot14()
        self.drawRegionBannerBoundingBox()
        self.drawRegionLegendIcon()
        self.drawRegionUsername()
        self.drawRegionHealthBar()
        self.drawRegionHelmetSlot()
        self.drawRegionArmorSlot()
        self.drawRegionKnockdownSlot()
        self.drawRegionBackpackSlot()
        self.drawRegionAbilityIcon()
        self.drawRegionBackButtonKeyBind()
        self.drawRegionBackButtonText()
        self.drawRegionGameMenuText()

    def drawRegionTopMenuInventoryText(self):
        pointA = (self.topMenuInventoryTextX1, self.topMenuInventoryTextY1)
        pointB = (pointA[0] + self.topMenuInventoryTextW, pointA[1] + self.topMenuInventoryTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionTopMenuSquadText(self):
        pointA = (self.topMenuSquadTextX1, self.topMenuSquadTextY1)
        pointB = (pointA[0] +  self.topMenuSquadTextW, pointA[1] + self.topMenuSquadTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionTopMenuLegendText(self):
        pointA = (self.topMenuLengendTextX1, self.topMenuLengendTextY1)
        pointB = (pointA[0] +  self.topMenuLengendTextW, pointA[1] + self.topMenuLengendTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1BoundingBox(self):
        pointA = (self.weapon1BoundingBoxX1, self.weapon1BoundingBoxY1)
        pointB = (pointA[0] +  self.weapon1BoundingBoxW, pointA[1] + self.weapon1BoundingBoxH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1KeyBindIcon(self):
        pointA = (self.weapon1KeyBindIconX1, self.weapon1KeyBindIconY1)
        pointB = (pointA[0] + self.weapon1KeyBindIconW, pointA[1] + self.weapon1KeyBindIconH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1Text(self):
        pointA = (self.weapon1TextX1, self.weapon1TextY1)
        pointB = (pointA[0] + self.weapon1TextW, pointA[1] + self.weapon1TextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1WeaponName(self):
        pointA = (self.weapon1WeaponNameX1, self.weapon1WeaponNameY1)
        pointB = (pointA[0] + self.weapon1WeaponNameW, pointA[1] + self.weapon1WeaponNameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1SkinName(self):
        pointA = (self.weapon1SkinNameX1, self.weapon1SkinNameY1)
        pointB = (pointA[0] + self.weapon1SkinNameW, pointA[1] + self.weapon1SkinNameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1ModSlot1(self):
        pointA = (self.weapon1ModSlot1X1, self.weapon1ModSlot1Y1)
        pointB = (pointA[0] + self.weapon1ModSlot1W, pointA[1] + self.weapon1ModSlot1H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1ModSlot2(self):
        pointA = (self.weapon1ModSlot2X1, self.weapon1ModSlot2Y1)
        pointB = (pointA[0] + self.weapon1ModSlot2W, pointA[1] + self.weapon1ModSlot2H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1ModSlot3(self):
        pointA = (self.weapon1ModSlot3X1, self.weapon1ModSlot3Y1)
        pointB = (pointA[0] + self.weapon1ModSlot3W, pointA[1] + self.weapon1ModSlot3H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1ModSlot4(self):
        pointA = (self.weapon1ModSlot4X1, self.weapon1ModSlot4Y1)
        pointB = (pointA[0] + self.weapon1ModSlot4W, pointA[1] + self.weapon1ModSlot4H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1ModSlot5(self):
        pointA = (self.weapon1ModSlot5X1, self.weapon1ModSlot5Y1)
        pointB = (pointA[0] + self.weapon1ModSlot5W, pointA[1] + self.weapon1ModSlot5H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1CurrentMagizineCount(self):
        pointA = (self.weapon1CurrentMagizineCountX1, self.weapon1CurrentMagizineCountY1)
        pointB = (pointA[0] + self.weapon1CurrentMagizineCountW, pointA[1] + self.weapon1CurrentMagizineCountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon1AmmoTypeIcon(self):
        pointA = (self.weapon1AmmoTypeIconX1, self.weapon1AmmoTypeIconY1)
        pointB = (pointA[0] + self.weapon1AmmoTypeIconW, pointA[1] + self.weapon1AmmoTypeIconH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2BoundingBox(self):
        pointA = (self.weapon2BoundingBoxX1, self.weapon2BoundingBoxY1)
        pointB = (pointA[0] + self.weapon2BoundingBoxW, pointA[1] + self.weapon2BoundingBoxH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2KeyBindIcon(self):
        pointA = (self.weapon2KeyBindIconX1, self.weapon2KeyBindIconY1)
        pointB = (pointA[0] + self.weapon2KeyBindIconW, pointA[1] + self.weapon2KeyBindIconH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2Text(self):
        pointA = (self.weapon2TextX1, self.weapon2TextY1)
        pointB = (pointA[0] + self.weapon2TextW, pointA[1] + self.weapon2TextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2WeaponIcon(self):
        pointA = (self.weapon2WeaponIconX1, self.weapon2WeaponIconY1)
        pointB = (pointA[0] + self.weapon2WeaponIconW, pointA[1] + self.weapon2WeaponIconH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2WeaponName(self):
        pointA = (self.weapon2WeaponNameX1, self.weapon2WeaponNameY1)
        pointB = (pointA[0] + self.weapon2WeaponNameW, pointA[1] + self.weapon2WeaponNameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2SkinName(self):
        pointA = (self.weapon2SkinNameX1, self.weapon2SkinNameY1)
        pointB = (pointA[0] + self.weapon2SkinNameW, pointA[1] + self.weapon2SkinNameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2ModSlot1(self):
        pointA = (self.weapon2ModSlot1X1, self.weapon2ModSlot1Y1)
        pointB = (pointA[0] + self.weapon2ModSlot1W, pointA[1] + self.weapon2ModSlot1H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2ModSlot2(self):
        pointA = (self.weapon2ModSlot2X1, self.weapon2ModSlot2Y1)
        pointB = (pointA[0] + self.weapon2ModSlot2W, pointA[1] + self.weapon2ModSlot2H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2ModSlot3(self):
        pointA = (self.weapon2ModSlot3X1, self.weapon2ModSlot3Y1)
        pointB = (pointA[0] + self.weapon2ModSlot3W, pointA[1] + self.weapon2ModSlot3H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2ModSlot4(self):
        pointA = (self.weapon2ModSlot4X1, self.weapon2ModSlot4Y1)
        pointB = (pointA[0] + self.weapon2ModSlot4W, pointA[1] + self.weapon2ModSlot4H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2ModSlot5(self):
        pointA = (self.weapon2ModSlot5X1, self.weapon2ModSlot5Y1)
        pointB = (pointA[0] + self.weapon2ModSlot5W, pointA[1] + self.weapon2ModSlot5H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2CurrentMagizineCount(self):
        pointA = (self.weapon2CurrentMagizineCountX1, self.weapon2CurrentMagizineCountY1)
        pointB = (pointA[0] + self.weapon2CurrentMagizineCountW, pointA[1] + self.weapon2CurrentMagizineCountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionWeapon2AmmoTypeIcon(self):
        pointA = (self.weapon2AmmoTypeIconX1, self.weapon2AmmoTypeIconY1)
        pointB = (pointA[0] + self.weapon2AmmoTypeIconW, pointA[1] + self.weapon2AmmoTypeIconH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot1(self):
        pointA = (self.backpackSlot1X1, self.backpackSlot1Y1)
        pointB = (pointA[0] + self.backpackSlot1W, pointA[1] + self.backpackSlot1H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2(self):
        pointA = (self.backpackSlot2X1, self.backpackSlot2Y1)
        pointB = (pointA[0] + self.backpackSlot2W, pointA[1] + self.backpackSlot2H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3(self):
        pointA = (self.backpackSlot3X1, self.backpackSlot3Y1)
        pointB = (pointA[0] + self.backpackSlot3W, pointA[1] + self.backpackSlot3H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4(self):
        pointA = (self.backpackSlot4X1, self.backpackSlot4Y1)
        pointB = (pointA[0] + self.backpackSlot4W, pointA[1] + self.backpackSlot4H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5(self):
        pointA = (self.backpackSlot5X1, self.backpackSlot5Y1)
        pointB = (pointA[0] + self.backpackSlot5W, pointA[1] + self.backpackSlot5H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6(self):
        pointA = (self.backpackSlot6X1, self.backpackSlot6Y1)
        pointB = (pointA[0] + self.backpackSlot6W, pointA[1] + self.backpackSlot6H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7(self):
        pointA = (self.backpackSlot7X1, self.backpackSlot7Y1)
        pointB = (pointA[0] + self.backpackSlot7W, pointA[1] + self.backpackSlot7H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8(self):
        pointA = (self.backpackSlot8X1, self.backpackSlot8Y1)
        pointB = (pointA[0] + self.backpackSlot8W, pointA[1] + self.backpackSlot8H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9(self):
        pointA = (self.backpackSlot9X1, self.backpackSlot9Y1)
        pointB = (pointA[0] + self.backpackSlot9W, pointA[1] + self.backpackSlot9H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10(self):
        pointA = (self.backpackSlot10X1, self.backpackSlot10Y1)
        pointB = (pointA[0] + self.backpackSlot10W, pointA[1] + self.backpackSlot10H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11(self):
        pointA = (self.backpackSlot11X1, self.backpackSlot11Y1)
        pointB = (pointA[0] + self.backpackSlot11W, pointA[1] + self.backpackSlot11H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12(self):
        pointA = (self.backpackSlot12X1, self.backpackSlot12Y1)
        pointB = (pointA[0] + self.backpackSlot12W, pointA[1] + self.backpackSlot12H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13(self):
        pointA = (self.backpackSlot13X1, self.backpackSlot13Y1)
        pointB = (pointA[0] + self.backpackSlot13W, pointA[1] + self.backpackSlot13H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14(self):
        pointA = (self.backpackSlot14X1, self.backpackSlot14Y1)
        pointB = (pointA[0] + self.backpackSlot14W, pointA[1] + self.backpackSlot14H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBannerBoundingBox(self):
        pointA = (self.bannerBoundingBoxX1, self.bannerBoundingBoxY1)
        pointB = (pointA[0] + self.bannerBoundingBoxW, pointA[1] + self.bannerBoundingBoxH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionLegendIcon(self):
        pointA = (self.legendIconX1, self.legendIconY1)
        pointB = (pointA[0] + self.legendIconW, pointA[1] + self.legendIconH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionUsername(self):
        pointA = (self.usernameX1, self.usernameY1)
        pointB = (pointA[0] + self.usernameW, pointA[1] + self.usernameH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionHealthBar(self):
        pointA = (self.healthBarX1, self.healthBarY1)
        pointB = (pointA[0] + self.healthBarW, pointA[1] + self.healthBarH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionHelmetSlot(self):
        pointA = (self.helmetSlotX1, self.helmetSlotY1)
        pointB = (pointA[0] + self.helmetSlotW, pointA[1] + self.helmetSlotH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionArmorSlot(self):
        pointA = (self.armorSlotX1, self.armorSlotY1)
        pointB = (pointA[0] + self.armorSlotW, pointA[1] + self.armorSlotH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionKnockdownSlot(self):
        pointA = (self.knockdownShieldSlotX1, self.knockdownShieldSlotY1)
        pointB = (pointA[0] + self.knockdownShieldSlotW, pointA[1] + self.knockdownShieldSlotH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot(self):
        pointA = (self.backpackSlotX1, self.backpackSlotY1)
        pointB = (pointA[0] + self.backpackSlotW, pointA[1] + self.backpackSlotH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionAbilityIcon(self):
        pointA = (self.abilityIconX1, self.abilityIconY1)
        pointB = (pointA[0] + self.abilityIconW, pointA[1] + self.abilityIconH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackButtonKeyBind(self):
        pointA = (self.backButtonKeyBindX1, self.backButtonKeyBindY1)
        pointB = (pointA[0] + self.backButtonKeyBindW, pointA[1] + self.backButtonKeyBindH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackButtonText(self):
        pointA = (self.backButtonTextX1, self.backButtonTextY1)
        pointB = (pointA[0] + self.backButtonTextW, pointA[1] + self.backButtonTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionGameMenuText(self):
        pointA = (self.gameMenuTextX1, self.gameMenuTextY1)
        pointB = (pointA[0] + self.gameMenuTextW, pointA[1] + self.gameMenuTextH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def getSimilarity(self, stringA, stringB):
        return SequenceMatcher(None, stringA, stringB).ratio()

    def getTopMenuInventoryTextSimilarity(self):
        pointA = (self.topMenuInventoryTextX1, self.topMenuInventoryTextY1)
        pointB = (pointA[0] + self.topMenuInventoryTextW, pointA[1] + self.topMenuInventoryTextH)

        inventoryTextImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedInventoryText = str(pytesseract.image_to_string(inventoryTextImage)).lower()
        return self.getSimilarity(processedInventoryText, "inventory")

    def getTopMenuSquadTextSimilarity(self):
        pointA = (self.topMenuSquadTextX1, self.topMenuSquadTextY1)
        pointB = (pointA[0] + self.topMenuSquadTextW, pointA[1] + self.topMenuSquadTextH)

        inventoryTextImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedInventoryText = str(pytesseract.image_to_string(inventoryTextImage)).lower()
        return self.getSimilarity(processedInventoryText, "squad")

    def getTopMenuLegendTextSimilarity(self):
        pointA = (self.topMenuLengendTextX1, self.topMenuLengendTextY1)
        pointB = (pointA[0] + self.topMenuLengendTextW, pointA[1] + self.topMenuLengendTextH)

        inventoryTextImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedInventoryText = str(pytesseract.image_to_string(inventoryTextImage)).lower()
        return self.getSimilarity(processedInventoryText, "legend")

    def getBackButtonTextSimilarity(self):
        pointA = (self.backButtonTextX1, self.backButtonTextY1)
        pointB = (pointA[0] + self.backButtonTextW, pointA[1] + self.backButtonTextH)

        inventoryTextImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedInventoryText = str(pytesseract.image_to_string(inventoryTextImage)).lower()
        return self.getSimilarity(processedInventoryText, "back")

    def getGameMenuTextSimilarity(self):
        pointA = (self.gameMenuTextX1, self.gameMenuTextY1)
        pointB = (pointA[0] + self.gameMenuTextW, pointA[1] + self.gameMenuTextH)

        inventoryTextImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedInventoryText = str(pytesseract.image_to_string(inventoryTextImage)).lower()
        return self.getSimilarity(processedInventoryText, "game menu")

    def getWeapon1TextSimilarity(self):
        pointA = (self.weapon1TextX1, self.weapon1TextY1)
        pointB = (pointA[0] + self.weapon1TextW, pointA[1] + self.weapon1TextH)

        inventoryTextImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedInventoryText = str(pytesseract.image_to_string(inventoryTextImage)).lower()
        return self.getSimilarity(processedInventoryText, "weapon")

    def getWeapon2TextSimilarity(self):
        pointA = (self.weapon2TextX1, self.weapon2TextY1)
        pointB = (pointA[0] + self.weapon2TextW, pointA[1] + self.weapon2TextH)

        inventoryTextImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        processedInventoryText = str(pytesseract.image_to_string(inventoryTextImage)).lower()
        return self.getSimilarity(processedInventoryText, "weapon")

    def isInInventoryUI(self):
        confidenceLevel = 0
        confidenceLevelRequirement = 4

        if(self.getTopMenuInventoryTextSimilarity() >= .80):
            confidenceLevel += 1

        if(self.getTopMenuSquadTextSimilarity() >= .80):
            confidenceLevel += 1

        if(self.getTopMenuLegendTextSimilarity() >= .80):
            confidenceLevel += 1

        if(self.getWeapon1TextSimilarity() >= .80):
            confidenceLevel += 1

        if(self.getWeapon2TextSimilarity() >= .80):
            confidenceLevel += 1

        if(self.getBackButtonTextSimilarity() >= .80):
            confidenceLevel += 1

        if(self.getGameMenuTextSimilarity() >= .80):
            confidenceLevel += 1

        print(confidenceLevel)
        print(self.getTopMenuInventoryTextSimilarity())
        print(self.getTopMenuSquadTextSimilarity())
        print(self.getTopMenuLegendTextSimilarity())
        print(self.getWeapon1TextSimilarity())
        print(self.getWeapon2TextSimilarity())
        print(self.getBackButtonTextSimilarity())
        print(self.getGameMenuTextSimilarity())

        return True if confidenceLevel >= confidenceLevelRequirement else False
