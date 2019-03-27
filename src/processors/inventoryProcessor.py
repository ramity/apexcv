import cv2
import pytesseract
from difflib import SequenceMatcher

class InventoryProcessor:

    image = None
    regionColor = (0, 0, 255)
    regionThickness = 1

    confidenceLevelRequirement = 4
    confidenceLevelOutput = True

    backpackSlotEmptyTemplatePath = "../input/templates/backpackSlotEmpty.jpg"
    backpackSlotEmptyTemplate = cv2.imread(backpackSlotEmptyTemplatePath, 0)

    backpackSlotLockedTemplatePath = "../input/templates/backpackSlotLocked.jpg"
    backpackSlotLockedTemplate = cv2.imread(backpackSlotLockedTemplatePath, 0)

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
    weapon1WeaponIconY1 = 200
    weapon1WeaponIconH = 100

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
    weapon2WeaponIconY1 = 200
    weapon2WeaponIconH = 100

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

    backpackSlot1AmmoTypeX1 = 614
    backpackSlot1AmmoTypeW = 92
    backpackSlot1AmmoTypeY1 = 590
    backpackSlot1AmmoTypeH = 58

    backpackSlot1AmmoAmountX1 = 674
    backpackSlot1AmmoAmountW = 28
    backpackSlot1AmmoAmountY1 = 647
    backpackSlot1AmmoAmountH = 20

    backpackSlot1AmmoBarsX1 = 619
    backpackSlot1AmmoBarsW = 81
    backpackSlot1AmmoBarsY1 = 671
    backpackSlot1AmmoBarsH = 5

    backpackSlot2X1 = 714
    backpackSlot2W = 92
    backpackSlot2Y1 = 590
    backpackSlot2H = 92

    backpackSlot2AmmoTypeX1 = 714
    backpackSlot2AmmoTypeW = 92
    backpackSlot2AmmoTypeY1 = 590
    backpackSlot2AmmoTypeH = 58

    backpackSlot2AmmoAmountX1 = 774
    backpackSlot2AmmoAmountW = 28
    backpackSlot2AmmoAmountY1 = 647
    backpackSlot2AmmoAmountH = 20

    backpackSlot2AmmoBarsX1 = 719
    backpackSlot2AmmoBarsW = 81
    backpackSlot2AmmoBarsY1 = 671
    backpackSlot2AmmoBarsH = 5

    backpackSlot3X1 = 814
    backpackSlot3W = 92
    backpackSlot3Y1 = 590
    backpackSlot3H = 92

    backpackSlot3AmmoTypeX1 = 814
    backpackSlot3AmmoTypeW = 92
    backpackSlot3AmmoTypeY1 = 590
    backpackSlot3AmmoTypeH = 58

    backpackSlot3AmmoAmountX1 = 874
    backpackSlot3AmmoAmountW = 28
    backpackSlot3AmmoAmountY1 = 647
    backpackSlot3AmmoAmountH = 20

    backpackSlot3AmmoBarsX1 = 819
    backpackSlot3AmmoBarsW = 81
    backpackSlot3AmmoBarsY1 = 671
    backpackSlot3AmmoBarsH = 5

    backpackSlot4X1 = 914
    backpackSlot4W = 92
    backpackSlot4Y1 = 590
    backpackSlot4H = 92

    backpackSlot4AmmoTypeX1 = 914
    backpackSlot4AmmoTypeW = 92
    backpackSlot4AmmoTypeY1 = 590
    backpackSlot4AmmoTypeH = 58

    backpackSlot4AmmoAmountX1 = 974
    backpackSlot4AmmoAmountW = 28
    backpackSlot4AmmoAmountY1 = 647
    backpackSlot4AmmoAmountH = 20

    backpackSlot4AmmoBarsX1 = 919
    backpackSlot4AmmoBarsW = 81
    backpackSlot4AmmoBarsY1 = 671
    backpackSlot4AmmoBarsH = 5

    backpackSlot5X1 = 1014
    backpackSlot5W = 92
    backpackSlot5Y1 = 590
    backpackSlot5H = 92

    backpackSlot5AmmoTypeX1 = 1014
    backpackSlot5AmmoTypeW = 92
    backpackSlot5AmmoTypeY1 = 590
    backpackSlot5AmmoTypeH = 58

    backpackSlot5AmmoAmountX1 = 1074
    backpackSlot5AmmoAmountW = 28
    backpackSlot5AmmoAmountY1 = 647
    backpackSlot5AmmoAmountH = 20

    backpackSlot5AmmoBarsX1 = 1019
    backpackSlot5AmmoBarsW = 81
    backpackSlot5AmmoBarsY1 = 671
    backpackSlot5AmmoBarsH = 5

    backpackSlot6X1 = 1114
    backpackSlot6W = 92
    backpackSlot6Y1 = 590
    backpackSlot6H = 92

    backpackSlot6AmmoTypeX1 = 1114
    backpackSlot6AmmoTypeW = 92
    backpackSlot6AmmoTypeY1 = 590
    backpackSlot6AmmoTypeH = 58

    backpackSlot6AmmoAmountX1 = 1174
    backpackSlot6AmmoAmountW = 28
    backpackSlot6AmmoAmountY1 = 647
    backpackSlot6AmmoAmountH = 20

    backpackSlot6AmmoBarsX1 = 1119
    backpackSlot6AmmoBarsW = 81
    backpackSlot6AmmoBarsY1 = 671
    backpackSlot6AmmoBarsH = 5

    backpackSlot7X1 = 1214
    backpackSlot7W = 92
    backpackSlot7Y1 = 590
    backpackSlot7H = 92

    backpackSlot7AmmoTypeX1 = 1214
    backpackSlot7AmmoTypeW = 92
    backpackSlot7AmmoTypeY1 = 590
    backpackSlot7AmmoTypeH = 58

    backpackSlot7AmmoAmountX1 = 1274
    backpackSlot7AmmoAmountW = 28
    backpackSlot7AmmoAmountY1 = 647
    backpackSlot7AmmoAmountH = 20

    backpackSlot7AmmoBarsX1 = 1219
    backpackSlot7AmmoBarsW = 81
    backpackSlot7AmmoBarsY1 = 671
    backpackSlot7AmmoBarsH = 5

    backpackSlot8X1 = 614
    backpackSlot8W = 92
    backpackSlot8Y1 = 690
    backpackSlot8H = 92

    backpackSlot8AmmoTypeX1 = 614
    backpackSlot8AmmoTypeW = 92
    backpackSlot8AmmoTypeY1 = 690
    backpackSlot8AmmoTypeH = 58

    backpackSlot8AmmoAmountX1 = 674
    backpackSlot8AmmoAmountW = 28
    backpackSlot8AmmoAmountY1 = 747
    backpackSlot8AmmoAmountH = 20

    backpackSlot8AmmoBarsX1 = 619
    backpackSlot8AmmoBarsW = 81
    backpackSlot8AmmoBarsY1 = 771
    backpackSlot8AmmoBarsH = 5

    backpackSlot9X1 = 714
    backpackSlot9W = 92
    backpackSlot9Y1 = 690
    backpackSlot9H = 92

    backpackSlot9AmmoTypeX1 = 714
    backpackSlot9AmmoTypeW = 92
    backpackSlot9AmmoTypeY1 = 690
    backpackSlot9AmmoTypeH = 58

    backpackSlot9AmmoAmountX1 = 774
    backpackSlot9AmmoAmountW = 28
    backpackSlot9AmmoAmountY1 = 747
    backpackSlot9AmmoAmountH = 20

    backpackSlot9AmmoBarsX1 = 719
    backpackSlot9AmmoBarsW = 81
    backpackSlot9AmmoBarsY1 = 771
    backpackSlot9AmmoBarsH = 5

    backpackSlot10X1 = 814
    backpackSlot10W = 92
    backpackSlot10Y1 = 690
    backpackSlot10H = 92

    backpackSlot10AmmoTypeX1 = 814
    backpackSlot10AmmoTypeW = 92
    backpackSlot10AmmoTypeY1 = 690
    backpackSlot10AmmoTypeH = 58

    backpackSlot10AmmoAmountX1 = 874
    backpackSlot10AmmoAmountW = 28
    backpackSlot10AmmoAmountY1 = 747
    backpackSlot10AmmoAmountH = 20

    backpackSlot10AmmoBarsX1 = 819
    backpackSlot10AmmoBarsW = 81
    backpackSlot10AmmoBarsY1 = 771
    backpackSlot10AmmoBarsH = 5

    backpackSlot11X1 = 914
    backpackSlot11W = 92
    backpackSlot11Y1 = 690
    backpackSlot11H = 92

    backpackSlot11AmmoTypeX1 = 914
    backpackSlot11AmmoTypeW = 92
    backpackSlot11AmmoTypeY1 = 690
    backpackSlot11AmmoTypeH = 58

    backpackSlot11AmmoAmountX1 = 974
    backpackSlot11AmmoAmountW = 28
    backpackSlot11AmmoAmountY1 = 747
    backpackSlot11AmmoAmountH = 20

    backpackSlot11AmmoBarsX1 = 919
    backpackSlot11AmmoBarsW = 81
    backpackSlot11AmmoBarsY1 = 771
    backpackSlot11AmmoBarsH = 5

    backpackSlot12X1 = 1014
    backpackSlot12W = 92
    backpackSlot12Y1 = 690
    backpackSlot12H = 92

    backpackSlot12AmmoTypeX1 = 1014
    backpackSlot12AmmoTypeW = 92
    backpackSlot12AmmoTypeY1 = 690
    backpackSlot12AmmoTypeH = 58

    backpackSlot12AmmoAmountX1 = 1074
    backpackSlot12AmmoAmountW = 28
    backpackSlot12AmmoAmountY1 = 747
    backpackSlot12AmmoAmountH = 20

    backpackSlot12AmmoBarsX1 = 1019
    backpackSlot12AmmoBarsW = 81
    backpackSlot12AmmoBarsY1 = 771
    backpackSlot12AmmoBarsH = 5

    backpackSlot13X1 = 1114
    backpackSlot13W = 92
    backpackSlot13Y1 = 690
    backpackSlot13H = 92

    backpackSlot13AmmoTypeX1 = 1114
    backpackSlot13AmmoTypeW = 92
    backpackSlot13AmmoTypeY1 = 690
    backpackSlot13AmmoTypeH = 58

    backpackSlot13AmmoAmountX1 = 1174
    backpackSlot13AmmoAmountW = 28
    backpackSlot13AmmoAmountY1 = 747
    backpackSlot13AmmoAmountH = 20

    backpackSlot13AmmoBarsX1 = 1119
    backpackSlot13AmmoBarsW = 81
    backpackSlot13AmmoBarsY1 = 771
    backpackSlot13AmmoBarsH = 5

    backpackSlot14X1 = 1214
    backpackSlot14W = 92
    backpackSlot14Y1 = 690
    backpackSlot14H = 92

    backpackSlot14AmmoTypeX1 = 1214
    backpackSlot14AmmoTypeW = 92
    backpackSlot14AmmoTypeY1 = 690
    backpackSlot14AmmoTypeH = 58

    backpackSlot14AmmoAmountX1 = 1274
    backpackSlot14AmmoAmountW = 28
    backpackSlot14AmmoAmountY1 = 747
    backpackSlot14AmmoAmountH = 20

    backpackSlot14AmmoBarsX1 = 1219
    backpackSlot14AmmoBarsW = 81
    backpackSlot14AmmoBarsY1 = 771
    backpackSlot14AmmoBarsH = 5

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

    backButtonTextX1 = 112
    backButtonTextW = 54
    backButtonTextY1 = 1036
    backButtonTextH = 24

    gameMenuTextX1 = 1739
    gameMenuTextW = 121
    gameMenuTextY1 = 1035
    gameMenuTextH = 25

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
        #self.drawRegionBackpackSlot1AmmoType()
        self.drawRegionBackpackSlot1AmmoAmount()
        self.drawRegionBackpackSlot1AmmoBars()
        self.drawRegionBackpackSlot2()
        self.drawRegionBackpackSlot2AmmoType()
        self.drawRegionBackpackSlot2AmmoAmount()
        self.drawRegionBackpackSlot2AmmoBars()
        self.drawRegionBackpackSlot3()
        self.drawRegionBackpackSlot3AmmoType()
        self.drawRegionBackpackSlot3AmmoAmount()
        self.drawRegionBackpackSlot3AmmoBars()
        self.drawRegionBackpackSlot4()
        self.drawRegionBackpackSlot4AmmoType()
        self.drawRegionBackpackSlot4AmmoAmount()
        self.drawRegionBackpackSlot4AmmoBars()
        self.drawRegionBackpackSlot5()
        self.drawRegionBackpackSlot5AmmoType()
        self.drawRegionBackpackSlot5AmmoAmount()
        self.drawRegionBackpackSlot5AmmoBars()
        self.drawRegionBackpackSlot6()
        self.drawRegionBackpackSlot6AmmoType()
        self.drawRegionBackpackSlot6AmmoAmount()
        self.drawRegionBackpackSlot6AmmoBars()
        self.drawRegionBackpackSlot7()
        self.drawRegionBackpackSlot7AmmoType()
        self.drawRegionBackpackSlot7AmmoAmount()
        self.drawRegionBackpackSlot7AmmoBars()
        self.drawRegionBackpackSlot8()
        self.drawRegionBackpackSlot8AmmoType()
        self.drawRegionBackpackSlot8AmmoAmount()
        self.drawRegionBackpackSlot8AmmoBars()
        self.drawRegionBackpackSlot9()
        self.drawRegionBackpackSlot9AmmoType()
        self.drawRegionBackpackSlot9AmmoAmount()
        self.drawRegionBackpackSlot9AmmoBars()
        self.drawRegionBackpackSlot10()
        self.drawRegionBackpackSlot10AmmoType()
        self.drawRegionBackpackSlot10AmmoAmount()
        self.drawRegionBackpackSlot10AmmoBars()
        self.drawRegionBackpackSlot11()
        self.drawRegionBackpackSlot11AmmoType()
        self.drawRegionBackpackSlot11AmmoAmount()
        self.drawRegionBackpackSlot11AmmoBars()
        self.drawRegionBackpackSlot12()
        self.drawRegionBackpackSlot12AmmoType()
        self.drawRegionBackpackSlot12AmmoAmount()
        self.drawRegionBackpackSlot12AmmoBars()
        self.drawRegionBackpackSlot13()
        self.drawRegionBackpackSlot13AmmoType()
        self.drawRegionBackpackSlot13AmmoAmount()
        self.drawRegionBackpackSlot13AmmoBars()
        self.drawRegionBackpackSlot14()
        self.drawRegionBackpackSlot14AmmoType()
        self.drawRegionBackpackSlot14AmmoAmount()
        self.drawRegionBackpackSlot14AmmoBars()
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

    def drawRegionBackpackSlot1AmmoType(self):
        pointA = (self.backpackSlot1AmmoTypeX1, self.backpackSlot1AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot1AmmoTypeW, pointA[1] + self.backpackSlot1AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot1AmmoAmount(self):
        pointA = (self.backpackSlot1AmmoAmountX1, self.backpackSlot1AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot1AmmoAmountW, pointA[1] + self.backpackSlot1AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot1AmmoBars(self):
        pointA = (self.backpackSlot1AmmoBarsX1, self.backpackSlot1AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot1AmmoBarsW, pointA[1] + self.backpackSlot1AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2(self):
        pointA = (self.backpackSlot2X1, self.backpackSlot2Y1)
        pointB = (pointA[0] + self.backpackSlot2W, pointA[1] + self.backpackSlot2H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2AmmoType(self):
        pointA = (self.backpackSlot2AmmoTypeX1, self.backpackSlot2AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot2AmmoTypeW, pointA[1] + self.backpackSlot2AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2AmmoAmount(self):
        pointA = (self.backpackSlot2AmmoAmountX1, self.backpackSlot2AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot2AmmoAmountW, pointA[1] + self.backpackSlot2AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2AmmoBars(self):
        pointA = (self.backpackSlot2AmmoBarsX1, self.backpackSlot2AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot2AmmoBarsW, pointA[1] + self.backpackSlot2AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3(self):
        pointA = (self.backpackSlot3X1, self.backpackSlot3Y1)
        pointB = (pointA[0] + self.backpackSlot3W, pointA[1] + self.backpackSlot3H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3AmmoType(self):
        pointA = (self.backpackSlot3AmmoTypeX1, self.backpackSlot3AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot3AmmoTypeW, pointA[1] + self.backpackSlot3AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3AmmoAmount(self):
        pointA = (self.backpackSlot3AmmoAmountX1, self.backpackSlot3AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot3AmmoAmountW, pointA[1] + self.backpackSlot3AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3AmmoBars(self):
        pointA = (self.backpackSlot3AmmoBarsX1, self.backpackSlot3AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot3AmmoBarsW, pointA[1] + self.backpackSlot3AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4(self):
        pointA = (self.backpackSlot4X1, self.backpackSlot4Y1)
        pointB = (pointA[0] + self.backpackSlot4W, pointA[1] + self.backpackSlot4H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4AmmoType(self):
        pointA = (self.backpackSlot4AmmoTypeX1, self.backpackSlot4AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot4AmmoTypeW, pointA[1] + self.backpackSlot4AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4AmmoAmount(self):
        pointA = (self.backpackSlot4AmmoAmountX1, self.backpackSlot4AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot4AmmoAmountW, pointA[1] + self.backpackSlot4AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4AmmoBars(self):
        pointA = (self.backpackSlot4AmmoBarsX1, self.backpackSlot4AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot4AmmoBarsW, pointA[1] + self.backpackSlot4AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5(self):
        pointA = (self.backpackSlot5X1, self.backpackSlot5Y1)
        pointB = (pointA[0] + self.backpackSlot5W, pointA[1] + self.backpackSlot5H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5AmmoType(self):
        pointA = (self.backpackSlot5AmmoTypeX1, self.backpackSlot5AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot5AmmoTypeW, pointA[1] + self.backpackSlot5AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5AmmoAmount(self):
        pointA = (self.backpackSlot5AmmoAmountX1, self.backpackSlot5AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot5AmmoAmountW, pointA[1] + self.backpackSlot5AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5AmmoBars(self):
        pointA = (self.backpackSlot5AmmoBarsX1, self.backpackSlot5AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot5AmmoBarsW, pointA[1] + self.backpackSlot5AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6(self):
        pointA = (self.backpackSlot6X1, self.backpackSlot6Y1)
        pointB = (pointA[0] + self.backpackSlot6W, pointA[1] + self.backpackSlot6H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6AmmoType(self):
        pointA = (self.backpackSlot6AmmoTypeX1, self.backpackSlot6AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot6AmmoTypeW, pointA[1] + self.backpackSlot6AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6AmmoAmount(self):
        pointA = (self.backpackSlot6AmmoAmountX1, self.backpackSlot6AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot6AmmoAmountW, pointA[1] + self.backpackSlot6AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6AmmoBars(self):
        pointA = (self.backpackSlot6AmmoBarsX1, self.backpackSlot6AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot6AmmoBarsW, pointA[1] + self.backpackSlot6AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7(self):
        pointA = (self.backpackSlot7X1, self.backpackSlot7Y1)
        pointB = (pointA[0] + self.backpackSlot7W, pointA[1] + self.backpackSlot7H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7AmmoType(self):
        pointA = (self.backpackSlot7AmmoTypeX1, self.backpackSlot7AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot7AmmoTypeW, pointA[1] + self.backpackSlot7AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7AmmoAmount(self):
        pointA = (self.backpackSlot7AmmoAmountX1, self.backpackSlot7AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot7AmmoAmountW, pointA[1] + self.backpackSlot7AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7AmmoBars(self):
        pointA = (self.backpackSlot7AmmoBarsX1, self.backpackSlot7AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot7AmmoBarsW, pointA[1] + self.backpackSlot7AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8(self):
        pointA = (self.backpackSlot8X1, self.backpackSlot8Y1)
        pointB = (pointA[0] + self.backpackSlot8W, pointA[1] + self.backpackSlot8H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8AmmoType(self):
        pointA = (self.backpackSlot8AmmoTypeX1, self.backpackSlot8AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot8AmmoTypeW, pointA[1] + self.backpackSlot8AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8AmmoAmount(self):
        pointA = (self.backpackSlot8AmmoAmountX1, self.backpackSlot8AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot8AmmoAmountW, pointA[1] + self.backpackSlot8AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8AmmoBars(self):
        pointA = (self.backpackSlot8AmmoBarsX1, self.backpackSlot8AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot8AmmoBarsW, pointA[1] + self.backpackSlot8AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9(self):
        pointA = (self.backpackSlot9X1, self.backpackSlot9Y1)
        pointB = (pointA[0] + self.backpackSlot9W, pointA[1] + self.backpackSlot9H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9AmmoType(self):
        pointA = (self.backpackSlot9AmmoTypeX1, self.backpackSlot9AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot9AmmoTypeW, pointA[1] + self.backpackSlot9AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9AmmoAmount(self):
        pointA = (self.backpackSlot9AmmoAmountX1, self.backpackSlot9AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot9AmmoAmountW, pointA[1] + self.backpackSlot9AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9AmmoBars(self):
        pointA = (self.backpackSlot9AmmoBarsX1, self.backpackSlot9AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot9AmmoBarsW, pointA[1] + self.backpackSlot9AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10(self):
        pointA = (self.backpackSlot10X1, self.backpackSlot10Y1)
        pointB = (pointA[0] + self.backpackSlot10W, pointA[1] + self.backpackSlot10H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10AmmoType(self):
        pointA = (self.backpackSlot10AmmoTypeX1, self.backpackSlot10AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot10AmmoTypeW, pointA[1] + self.backpackSlot10AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10AmmoAmount(self):
        pointA = (self.backpackSlot10AmmoAmountX1, self.backpackSlot10AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot10AmmoAmountW, pointA[1] + self.backpackSlot10AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10AmmoBars(self):
        pointA = (self.backpackSlot10AmmoBarsX1, self.backpackSlot10AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot10AmmoBarsW, pointA[1] + self.backpackSlot10AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11(self):
        pointA = (self.backpackSlot11X1, self.backpackSlot11Y1)
        pointB = (pointA[0] + self.backpackSlot11W, pointA[1] + self.backpackSlot11H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11AmmoType(self):
        pointA = (self.backpackSlot11AmmoTypeX1, self.backpackSlot11AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot11AmmoTypeW, pointA[1] + self.backpackSlot11AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11AmmoAmount(self):
        pointA = (self.backpackSlot11AmmoAmountX1, self.backpackSlot11AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot11AmmoAmountW, pointA[1] + self.backpackSlot11AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11AmmoBars(self):
        pointA = (self.backpackSlot11AmmoBarsX1, self.backpackSlot11AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot11AmmoBarsW, pointA[1] + self.backpackSlot11AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12(self):
        pointA = (self.backpackSlot12X1, self.backpackSlot12Y1)
        pointB = (pointA[0] + self.backpackSlot12W, pointA[1] + self.backpackSlot12H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12AmmoType(self):
        pointA = (self.backpackSlot12AmmoTypeX1, self.backpackSlot12AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot12AmmoTypeW, pointA[1] + self.backpackSlot12AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12AmmoAmount(self):
        pointA = (self.backpackSlot12AmmoAmountX1, self.backpackSlot12AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot12AmmoAmountW, pointA[1] + self.backpackSlot12AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12AmmoBars(self):
        pointA = (self.backpackSlot12AmmoBarsX1, self.backpackSlot12AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot12AmmoBarsW, pointA[1] + self.backpackSlot12AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13(self):
        pointA = (self.backpackSlot13X1, self.backpackSlot13Y1)
        pointB = (pointA[0] + self.backpackSlot13W, pointA[1] + self.backpackSlot13H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13AmmoType(self):
        pointA = (self.backpackSlot13AmmoTypeX1, self.backpackSlot13AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot13AmmoTypeW, pointA[1] + self.backpackSlot13AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13AmmoAmount(self):
        pointA = (self.backpackSlot13AmmoAmountX1, self.backpackSlot13AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot13AmmoAmountW, pointA[1] + self.backpackSlot13AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13AmmoBars(self):
        pointA = (self.backpackSlot13AmmoBarsX1, self.backpackSlot13AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot13AmmoBarsW, pointA[1] + self.backpackSlot13AmmoBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14(self):
        pointA = (self.backpackSlot14X1, self.backpackSlot14Y1)
        pointB = (pointA[0] + self.backpackSlot14W, pointA[1] + self.backpackSlot14H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14AmmoType(self):
        pointA = (self.backpackSlot14AmmoTypeX1, self.backpackSlot14AmmoTypeY1)
        pointB = (pointA[0] + self.backpackSlot14AmmoTypeW, pointA[1] + self.backpackSlot14AmmoTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14AmmoAmount(self):
        pointA = (self.backpackSlot14AmmoAmountX1, self.backpackSlot14AmmoAmountY1)
        pointB = (pointA[0] + self.backpackSlot14AmmoAmountW, pointA[1] + self.backpackSlot14AmmoAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14AmmoBars(self):
        pointA = (self.backpackSlot14AmmoBarsX1, self.backpackSlot14AmmoBarsY1)
        pointB = (pointA[0] + self.backpackSlot14AmmoBarsW, pointA[1] + self.backpackSlot14AmmoBarsH)
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

        topMenuInventoryTextSimilarity = self.getTopMenuInventoryTextSimilarity()
        topMenuSquadTextSimilarity = self.getTopMenuSquadTextSimilarity()
        topMenuLegendTextSimilarity = self.getTopMenuLegendTextSimilarity()
        weapon1TextSimilarity = self.getWeapon1TextSimilarity()
        weapon2TextSimilarity = self.getWeapon2TextSimilarity()
        backButtonTextSimilarity = self.getBackButtonTextSimilarity()
        gameMenuTextSimilarity = self.getGameMenuTextSimilarity()

        if(topMenuInventoryTextSimilarity >= .80):
            confidenceLevel += 1
        if(topMenuSquadTextSimilarity >= .80):
            confidenceLevel += 1
        if(topMenuLegendTextSimilarity >= .80):
            confidenceLevel += 1
        if(weapon1TextSimilarity >= .80):
            confidenceLevel += 1
        if(weapon2TextSimilarity >= .80):
            confidenceLevel += 1
        if(backButtonTextSimilarity >= .80):
            confidenceLevel += 1
        if(gameMenuTextSimilarity >= .80):
            confidenceLevel += 1

        if(self.confidenceLevelOutput):
            print("confidenceLevel: ", confidenceLevel)
            print("confidenceLevelRequirement: ", self.confidenceLevelRequirement)
            print("topMenuInventoryTextSimilarity: ", topMenuInventoryTextSimilarity)
            print("topMenuSquadTextSimilarity: ", topMenuSquadTextSimilarity)
            print("topMenuLegendTextSimilarity: ", topMenuLegendTextSimilarity)
            print("weapon1TextSimilarity: ", weapon1TextSimilarity)
            print("weapon2TextSimilarity: ", weapon2TextSimilarity)
            print("backButtonTextSimilarity: ", backButtonTextSimilarity)
            print("gameMenuTextSimilarity: ", gameMenuTextSimilarity)

        return True if confidenceLevel >= self.confidenceLevelRequirement else False

    def isBackpackSlot5Locked(self):
        pointA = (self.backpackSlot5X1, self.backpackSlot5Y1)
        pointB = (pointA[0] + self.backpackSlot5W, pointA[1] + self.backpackSlot5H)

        backpackSlot5Image = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        grayBackpackSlot5Image = cv2.cvtColor(backpackSlot5Image, cv2.COLOR_BGR2GRAY)

        isLockedResult = cv2.matchTemplate(grayBackpackSlot5Image, self.backpackSlotLockedTemplate, cv2.TM_CCOEFF)
        isEmptyResult = cv2.matchTemplate(grayBackpackSlot5Image, self.backpackSlotEmptyTemplate, cv2.TM_CCOEFF)

        isLockedMaxValue = cv2.minMaxLoc(isLockedResult)[1]
        isEmptyMaxValue = cv2.minMaxLoc(isEmptyResult)[1]

        return True if isLockedMaxValue > isEmptyMaxValue else False

    def isBackpackSlot6Locked(self):
        pointA = (self.backpackSlot6X1, self.backpackSlot6Y1)
        pointB = (pointA[0] + self.backpackSlot6W, pointA[1] + self.backpackSlot6H)

        backpackSlot6Image = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        grayBackpackSlot6Image = cv2.cvtColor(backpackSlot6Image, cv2.COLOR_BGR2GRAY)

        isLockedResult = cv2.matchTemplate(grayBackpackSlot6Image, self.backpackSlotLockedTemplate, cv2.TM_CCOEFF)
        isEmptyResult = cv2.matchTemplate(grayBackpackSlot6Image, self.backpackSlotEmptyTemplate, cv2.TM_CCOEFF)

        isLockedMaxValue = cv2.minMaxLoc(isLockedResult)[1]
        isEmptyMaxValue = cv2.minMaxLoc(isEmptyResult)[1]

        return True if isLockedMaxValue > isEmptyMaxValue else False

    def isBackpackSlot7Locked(self):
        pointA = (self.backpackSlot7X1, self.backpackSlot7Y1)
        pointB = (pointA[0] + self.backpackSlot7W, pointA[1] + self.backpackSlot7H)

        backpackSlot7Image = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        grayBackpackSlot7Image = cv2.cvtColor(backpackSlot7Image, cv2.COLOR_BGR2GRAY)

        isLockedResult = cv2.matchTemplate(grayBackpackSlot7Image, self.backpackSlotLockedTemplate, cv2.TM_CCOEFF)
        isEmptyResult = cv2.matchTemplate(grayBackpackSlot7Image, self.backpackSlotEmptyTemplate, cv2.TM_CCOEFF)

        isLockedMaxValue = cv2.minMaxLoc(isLockedResult)[1]
        isEmptyMaxValue = cv2.minMaxLoc(isEmptyResult)[1]

        return True if isLockedMaxValue > isEmptyMaxValue else False

    def isBackpackSlot12Locked(self):
        pointA = (self.backpackSlot12X1, self.backpackSlot12Y1)
        pointB = (pointA[0] + self.backpackSlot12W, pointA[1] + self.backpackSlot12H)

        backpackSlot12Image = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        grayBackpackSlot12Image = cv2.cvtColor(backpackSlot12Image, cv2.COLOR_BGR2GRAY)

        isLockedResult = cv2.matchTemplate(grayBackpackSlot12Image, self.backpackSlotLockedTemplate, cv2.TM_CCOEFF)
        isEmptyResult = cv2.matchTemplate(grayBackpackSlot12Image, self.backpackSlotEmptyTemplate, cv2.TM_CCOEFF)

        isLockedMaxValue = cv2.minMaxLoc(isLockedResult)[1]
        isEmptyMaxValue = cv2.minMaxLoc(isEmptyResult)[1]

        return True if isLockedMaxValue > isEmptyMaxValue else False

    def isBackpackSlot13Locked(self):
        pointA = (self.backpackSlot13X1, self.backpackSlot13Y1)
        pointB = (pointA[0] + self.backpackSlot13W, pointA[1] + self.backpackSlot13H)

        backpackSlot13Image = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        grayBackpackSlot13Image = cv2.cvtColor(backpackSlot13Image, cv2.COLOR_BGR2GRAY)

        isLockedResult = cv2.matchTemplate(grayBackpackSlot13Image, self.backpackSlotLockedTemplate, cv2.TM_CCOEFF)
        isEmptyResult = cv2.matchTemplate(grayBackpackSlot13Image, self.backpackSlotEmptyTemplate, cv2.TM_CCOEFF)

        isLockedMaxValue = cv2.minMaxLoc(isLockedResult)[1]
        isEmptyMaxValue = cv2.minMaxLoc(isEmptyResult)[1]

        return True if isLockedMaxValue > isEmptyMaxValue else False

    def isBackpackSlot14Locked(self):
        pointA = (self.backpackSlot14X1, self.backpackSlot14Y1)
        pointB = (pointA[0] + self.backpackSlot14W, pointA[1] + self.backpackSlot14H)

        backpackSlot14Image = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        grayBackpackSlot14Image = cv2.cvtColor(backpackSlot14Image, cv2.COLOR_BGR2GRAY)

        isLockedResult = cv2.matchTemplate(grayBackpackSlot14Image, self.backpackSlotLockedTemplate, cv2.TM_CCOEFF)
        isEmptyResult = cv2.matchTemplate(grayBackpackSlot14Image, self.backpackSlotEmptyTemplate, cv2.TM_CCOEFF)

        isLockedMaxValue = cv2.minMaxLoc(isLockedResult)[1]
        isEmptyMaxValue = cv2.minMaxLoc(isEmptyResult)[1]

        return True if isLockedMaxValue > isEmptyMaxValue else False
