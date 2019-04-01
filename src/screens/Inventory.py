import cv2
import pytesseract
from Base import Base

class Inventory(Base):

    confidenceLevelRequirement = 6
    confidenceLevelOutput = False

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

    weapon1SkinNameX1 = 419
    weapon1SkinNameW = 152
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

    weapon1AmmoTypeIconX1 = 833
    weapon1AmmoTypeIconW = 76
    weapon1AmmoTypeIconY1 = 376
    weapon1AmmoTypeIconH = 73

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

    weapon2SkinNameX1 = 1009
    weapon2SkinNameW = 152
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

    weapon2AmmoTypeIconX1 = 1423
    weapon2AmmoTypeIconW = 76
    weapon2AmmoTypeIconY1 = 376
    weapon2AmmoTypeIconH = 73

    backpackSlot1X1 = 614
    backpackSlot1W = 92
    backpackSlot1Y1 = 590
    backpackSlot1H = 92

    backpackSlot1ItemTypeX1 = 614
    backpackSlot1ItemTypeW = 92
    backpackSlot1ItemTypeY1 = 590
    backpackSlot1ItemTypeH = 58

    backpackSlot1ItemAmountX1 = 674
    backpackSlot1ItemAmountW = 28
    backpackSlot1ItemAmountY1 = 647
    backpackSlot1ItemAmountH = 20

    backpackSlot1ItemBarsX1 = 619
    backpackSlot1ItemBarsW = 81
    backpackSlot1ItemBarsY1 = 671
    backpackSlot1ItemBarsH = 5

    backpackSlot2X1 = 714
    backpackSlot2W = 92
    backpackSlot2Y1 = 590
    backpackSlot2H = 92

    backpackSlot2ItemTypeX1 = 714
    backpackSlot2ItemTypeW = 92
    backpackSlot2ItemTypeY1 = 590
    backpackSlot2ItemTypeH = 58

    backpackSlot2ItemAmountX1 = 774
    backpackSlot2ItemAmountW = 28
    backpackSlot2ItemAmountY1 = 647
    backpackSlot2ItemAmountH = 20

    backpackSlot2ItemBarsX1 = 719
    backpackSlot2ItemBarsW = 81
    backpackSlot2ItemBarsY1 = 671
    backpackSlot2ItemBarsH = 5

    backpackSlot3X1 = 814
    backpackSlot3W = 92
    backpackSlot3Y1 = 590
    backpackSlot3H = 92

    backpackSlot3ItemTypeX1 = 814
    backpackSlot3ItemTypeW = 92
    backpackSlot3ItemTypeY1 = 590
    backpackSlot3ItemTypeH = 58

    backpackSlot3ItemAmountX1 = 874
    backpackSlot3ItemAmountW = 28
    backpackSlot3ItemAmountY1 = 647
    backpackSlot3ItemAmountH = 20

    backpackSlot3ItemBarsX1 = 819
    backpackSlot3ItemBarsW = 81
    backpackSlot3ItemBarsY1 = 671
    backpackSlot3ItemBarsH = 5

    backpackSlot4X1 = 914
    backpackSlot4W = 92
    backpackSlot4Y1 = 590
    backpackSlot4H = 92

    backpackSlot4ItemTypeX1 = 914
    backpackSlot4ItemTypeW = 92
    backpackSlot4ItemTypeY1 = 590
    backpackSlot4ItemTypeH = 58

    backpackSlot4ItemAmountX1 = 974
    backpackSlot4ItemAmountW = 28
    backpackSlot4ItemAmountY1 = 647
    backpackSlot4ItemAmountH = 20

    backpackSlot4ItemBarsX1 = 919
    backpackSlot4ItemBarsW = 81
    backpackSlot4ItemBarsY1 = 671
    backpackSlot4ItemBarsH = 5

    backpackSlot5X1 = 1014
    backpackSlot5W = 92
    backpackSlot5Y1 = 590
    backpackSlot5H = 92

    backpackSlot5ItemTypeX1 = 1014
    backpackSlot5ItemTypeW = 92
    backpackSlot5ItemTypeY1 = 590
    backpackSlot5ItemTypeH = 58

    backpackSlot5ItemAmountX1 = 1074
    backpackSlot5ItemAmountW = 28
    backpackSlot5ItemAmountY1 = 647
    backpackSlot5ItemAmountH = 20

    backpackSlot5ItemBarsX1 = 1019
    backpackSlot5ItemBarsW = 81
    backpackSlot5ItemBarsY1 = 671
    backpackSlot5ItemBarsH = 5

    backpackSlot6X1 = 1114
    backpackSlot6W = 92
    backpackSlot6Y1 = 590
    backpackSlot6H = 92

    backpackSlot6ItemTypeX1 = 1114
    backpackSlot6ItemTypeW = 92
    backpackSlot6ItemTypeY1 = 590
    backpackSlot6ItemTypeH = 58

    backpackSlot6ItemAmountX1 = 1174
    backpackSlot6ItemAmountW = 28
    backpackSlot6ItemAmountY1 = 647
    backpackSlot6ItemAmountH = 20

    backpackSlot6ItemBarsX1 = 1119
    backpackSlot6ItemBarsW = 81
    backpackSlot6ItemBarsY1 = 671
    backpackSlot6ItemBarsH = 5

    backpackSlot7X1 = 1214
    backpackSlot7W = 92
    backpackSlot7Y1 = 590
    backpackSlot7H = 92

    backpackSlot7ItemTypeX1 = 1214
    backpackSlot7ItemTypeW = 92
    backpackSlot7ItemTypeY1 = 590
    backpackSlot7ItemTypeH = 58

    backpackSlot7ItemAmountX1 = 1274
    backpackSlot7ItemAmountW = 28
    backpackSlot7ItemAmountY1 = 647
    backpackSlot7ItemAmountH = 20

    backpackSlot7ItemBarsX1 = 1219
    backpackSlot7ItemBarsW = 81
    backpackSlot7ItemBarsY1 = 671
    backpackSlot7ItemBarsH = 5

    backpackSlot8X1 = 614
    backpackSlot8W = 92
    backpackSlot8Y1 = 690
    backpackSlot8H = 92

    backpackSlot8ItemTypeX1 = 614
    backpackSlot8ItemTypeW = 92
    backpackSlot8ItemTypeY1 = 690
    backpackSlot8ItemTypeH = 58

    backpackSlot8ItemAmountX1 = 674
    backpackSlot8ItemAmountW = 28
    backpackSlot8ItemAmountY1 = 747
    backpackSlot8ItemAmountH = 20

    backpackSlot8ItemBarsX1 = 619
    backpackSlot8ItemBarsW = 81
    backpackSlot8ItemBarsY1 = 771
    backpackSlot8ItemBarsH = 5

    backpackSlot9X1 = 714
    backpackSlot9W = 92
    backpackSlot9Y1 = 690
    backpackSlot9H = 92

    backpackSlot9ItemTypeX1 = 714
    backpackSlot9ItemTypeW = 92
    backpackSlot9ItemTypeY1 = 690
    backpackSlot9ItemTypeH = 58

    backpackSlot9ItemAmountX1 = 774
    backpackSlot9ItemAmountW = 28
    backpackSlot9ItemAmountY1 = 747
    backpackSlot9ItemAmountH = 20

    backpackSlot9ItemBarsX1 = 719
    backpackSlot9ItemBarsW = 81
    backpackSlot9ItemBarsY1 = 771
    backpackSlot9ItemBarsH = 5

    backpackSlot10X1 = 814
    backpackSlot10W = 92
    backpackSlot10Y1 = 690
    backpackSlot10H = 92

    backpackSlot10ItemTypeX1 = 814
    backpackSlot10ItemTypeW = 92
    backpackSlot10ItemTypeY1 = 690
    backpackSlot10ItemTypeH = 58

    backpackSlot10ItemAmountX1 = 874
    backpackSlot10ItemAmountW = 28
    backpackSlot10ItemAmountY1 = 747
    backpackSlot10ItemAmountH = 20

    backpackSlot10ItemBarsX1 = 819
    backpackSlot10ItemBarsW = 81
    backpackSlot10ItemBarsY1 = 771
    backpackSlot10ItemBarsH = 5

    backpackSlot11X1 = 914
    backpackSlot11W = 92
    backpackSlot11Y1 = 690
    backpackSlot11H = 92

    backpackSlot11ItemTypeX1 = 914
    backpackSlot11ItemTypeW = 92
    backpackSlot11ItemTypeY1 = 690
    backpackSlot11ItemTypeH = 58

    backpackSlot11ItemAmountX1 = 974
    backpackSlot11ItemAmountW = 28
    backpackSlot11ItemAmountY1 = 747
    backpackSlot11ItemAmountH = 20

    backpackSlot11ItemBarsX1 = 919
    backpackSlot11ItemBarsW = 81
    backpackSlot11ItemBarsY1 = 771
    backpackSlot11ItemBarsH = 5

    backpackSlot12X1 = 1014
    backpackSlot12W = 92
    backpackSlot12Y1 = 690
    backpackSlot12H = 92

    backpackSlot12ItemTypeX1 = 1014
    backpackSlot12ItemTypeW = 92
    backpackSlot12ItemTypeY1 = 690
    backpackSlot12ItemTypeH = 58

    backpackSlot12ItemAmountX1 = 1074
    backpackSlot12ItemAmountW = 28
    backpackSlot12ItemAmountY1 = 747
    backpackSlot12ItemAmountH = 20

    backpackSlot12ItemBarsX1 = 1019
    backpackSlot12ItemBarsW = 81
    backpackSlot12ItemBarsY1 = 771
    backpackSlot12ItemBarsH = 5

    backpackSlot13X1 = 1114
    backpackSlot13W = 92
    backpackSlot13Y1 = 690
    backpackSlot13H = 92

    backpackSlot13ItemTypeX1 = 1114
    backpackSlot13ItemTypeW = 92
    backpackSlot13ItemTypeY1 = 690
    backpackSlot13ItemTypeH = 58

    backpackSlot13ItemAmountX1 = 1174
    backpackSlot13ItemAmountW = 28
    backpackSlot13ItemAmountY1 = 747
    backpackSlot13ItemAmountH = 20

    backpackSlot13ItemBarsX1 = 1119
    backpackSlot13ItemBarsW = 81
    backpackSlot13ItemBarsY1 = 771
    backpackSlot13ItemBarsH = 5

    backpackSlot14X1 = 1214
    backpackSlot14W = 92
    backpackSlot14Y1 = 690
    backpackSlot14H = 92

    backpackSlot14ItemTypeX1 = 1214
    backpackSlot14ItemTypeW = 92
    backpackSlot14ItemTypeY1 = 690
    backpackSlot14ItemTypeH = 58

    backpackSlot14ItemAmountX1 = 1274
    backpackSlot14ItemAmountW = 28
    backpackSlot14ItemAmountY1 = 747
    backpackSlot14ItemAmountH = 20

    backpackSlot14ItemBarsX1 = 1219
    backpackSlot14ItemBarsW = 81
    backpackSlot14ItemBarsY1 = 771
    backpackSlot14ItemBarsH = 5

    teammate1BannerBoundingBoxX1 = 46
    teammate1BannerBoundingBoxW = 415
    teammate1BannerBoundingBoxY1 = 678
    teammate1BannerBoundingBoxH = 50

    teammate1LegendIconX1 = 75
    teammate1LegendIconW = 45
    teammate1LegendIconY1 = 680
    teammate1LegendIconH = 45

    # teammate1 stuff goes here

    teammate2BannerBoundingBoxX1 = 46
    teammate2BannerBoundingBoxW = 415
    teammate2BannerBoundingBoxY1 = 738
    teammate2BannerBoundingBoxH = 50

    teammate2LegendIconX1 = 75
    teammate2LegendIconW = 45
    teammate2LegendIconY1 = 740
    teammate2LegendIconH = 45

    # teammate2 stuff goes here

    bannerBoundingBoxX1 = 46
    bannerBoundingBoxW = 468
    bannerBoundingBoxY1 = 838
    bannerBoundingBoxH = 91

    legendIconX1 = 104
    legendIconW = 86
    legendIconY1 = 840
    legendIconH = 86

    usernameX1 = 198
    usernameW = 232
    usernameY1 = 850
    usernameH = 29

    shieldBarX1 = 199
    shieldBarW = 232
    shieldBarY1 = 889
    shieldBarH = 8

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

    abilityPercentTextX1 = 1452
    abilityPercentTextW = 48
    abilityPercentTextY1 = 941
    abilityPercentTextH = 27

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

    def drawRegions(self):
        self.drawRegionTopMenuInventoryText()
        self.drawRegionTopMenuSquadText()
        self.drawRegionTopMenuLegendText()
        self.drawRegionWeapon1BoundingBox()
        self.drawRegionWeapon1KeyBindIcon()
        self.drawRegionWeapon1Text()
        self.drawRegionWeapon1WeaponIcon()
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
        #self.drawRegionBackpackSlot1ItemType()
        self.drawRegionBackpackSlot1ItemAmount()
        self.drawRegionBackpackSlot1ItemBars()
        self.drawRegionBackpackSlot2()
        self.drawRegionBackpackSlot2ItemType()
        self.drawRegionBackpackSlot2ItemAmount()
        self.drawRegionBackpackSlot2ItemBars()
        self.drawRegionBackpackSlot3()
        self.drawRegionBackpackSlot3ItemType()
        self.drawRegionBackpackSlot3ItemAmount()
        self.drawRegionBackpackSlot3ItemBars()
        self.drawRegionBackpackSlot4()
        self.drawRegionBackpackSlot4ItemType()
        self.drawRegionBackpackSlot4ItemAmount()
        self.drawRegionBackpackSlot4ItemBars()
        self.drawRegionBackpackSlot5()
        self.drawRegionBackpackSlot5ItemType()
        self.drawRegionBackpackSlot5ItemAmount()
        self.drawRegionBackpackSlot5ItemBars()
        self.drawRegionBackpackSlot6()
        self.drawRegionBackpackSlot6ItemType()
        self.drawRegionBackpackSlot6ItemAmount()
        self.drawRegionBackpackSlot6ItemBars()
        self.drawRegionBackpackSlot7()
        self.drawRegionBackpackSlot7ItemType()
        self.drawRegionBackpackSlot7ItemAmount()
        self.drawRegionBackpackSlot7ItemBars()
        self.drawRegionBackpackSlot8()
        self.drawRegionBackpackSlot8ItemType()
        self.drawRegionBackpackSlot8ItemAmount()
        self.drawRegionBackpackSlot8ItemBars()
        self.drawRegionBackpackSlot9()
        self.drawRegionBackpackSlot9ItemType()
        self.drawRegionBackpackSlot9ItemAmount()
        self.drawRegionBackpackSlot9ItemBars()
        self.drawRegionBackpackSlot10()
        self.drawRegionBackpackSlot10ItemType()
        self.drawRegionBackpackSlot10ItemAmount()
        self.drawRegionBackpackSlot10ItemBars()
        self.drawRegionBackpackSlot11()
        self.drawRegionBackpackSlot11ItemType()
        self.drawRegionBackpackSlot11ItemAmount()
        self.drawRegionBackpackSlot11ItemBars()
        self.drawRegionBackpackSlot12()
        self.drawRegionBackpackSlot12ItemType()
        self.drawRegionBackpackSlot12ItemAmount()
        self.drawRegionBackpackSlot12ItemBars()
        self.drawRegionBackpackSlot13()
        self.drawRegionBackpackSlot13ItemType()
        self.drawRegionBackpackSlot13ItemAmount()
        self.drawRegionBackpackSlot13ItemBars()
        self.drawRegionBackpackSlot14()
        self.drawRegionBackpackSlot14ItemType()
        self.drawRegionBackpackSlot14ItemAmount()
        self.drawRegionBackpackSlot14ItemBars()
        self.drawRegionBannerBoundingBox()
        self.drawRegionLegendIcon()
        self.drawRegionUsername()
        self.drawRegionShieldBar()
        self.drawRegionHealthBar()
        self.drawRegionHelmetSlot()
        self.drawRegionArmorSlot()
        self.drawRegionKnockdownSlot()
        self.drawRegionBackpackSlot()
        self.drawRegionAbilityIcon()
        self.drawRegionAbilityPercentText()
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

    def drawRegionWeapon1WeaponIcon(self):
        pointA = (self.weapon1WeaponIconX1, self.weapon1WeaponIconY1)
        pointB = (pointA[0] + self.weapon1WeaponIconW, pointA[1] + self.weapon1WeaponIconH)
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

    def drawRegionBackpackSlot1ItemType(self):
        pointA = (self.backpackSlot1ItemTypeX1, self.backpackSlot1ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot1ItemTypeW, pointA[1] + self.backpackSlot1ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot1ItemAmount(self):
        pointA = (self.backpackSlot1ItemAmountX1, self.backpackSlot1ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot1ItemAmountW, pointA[1] + self.backpackSlot1ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot1ItemBars(self):
        pointA = (self.backpackSlot1ItemBarsX1, self.backpackSlot1ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot1ItemBarsW, pointA[1] + self.backpackSlot1ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2(self):
        pointA = (self.backpackSlot2X1, self.backpackSlot2Y1)
        pointB = (pointA[0] + self.backpackSlot2W, pointA[1] + self.backpackSlot2H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2ItemType(self):
        pointA = (self.backpackSlot2ItemTypeX1, self.backpackSlot2ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot2ItemTypeW, pointA[1] + self.backpackSlot2ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2ItemAmount(self):
        pointA = (self.backpackSlot2ItemAmountX1, self.backpackSlot2ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot2ItemAmountW, pointA[1] + self.backpackSlot2ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot2ItemBars(self):
        pointA = (self.backpackSlot2ItemBarsX1, self.backpackSlot2ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot2ItemBarsW, pointA[1] + self.backpackSlot2ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3(self):
        pointA = (self.backpackSlot3X1, self.backpackSlot3Y1)
        pointB = (pointA[0] + self.backpackSlot3W, pointA[1] + self.backpackSlot3H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3ItemType(self):
        pointA = (self.backpackSlot3ItemTypeX1, self.backpackSlot3ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot3ItemTypeW, pointA[1] + self.backpackSlot3ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3ItemAmount(self):
        pointA = (self.backpackSlot3ItemAmountX1, self.backpackSlot3ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot3ItemAmountW, pointA[1] + self.backpackSlot3ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot3ItemBars(self):
        pointA = (self.backpackSlot3ItemBarsX1, self.backpackSlot3ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot3ItemBarsW, pointA[1] + self.backpackSlot3ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4(self):
        pointA = (self.backpackSlot4X1, self.backpackSlot4Y1)
        pointB = (pointA[0] + self.backpackSlot4W, pointA[1] + self.backpackSlot4H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4ItemType(self):
        pointA = (self.backpackSlot4ItemTypeX1, self.backpackSlot4ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot4ItemTypeW, pointA[1] + self.backpackSlot4ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4ItemAmount(self):
        pointA = (self.backpackSlot4ItemAmountX1, self.backpackSlot4ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot4ItemAmountW, pointA[1] + self.backpackSlot4ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot4ItemBars(self):
        pointA = (self.backpackSlot4ItemBarsX1, self.backpackSlot4ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot4ItemBarsW, pointA[1] + self.backpackSlot4ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5(self):
        pointA = (self.backpackSlot5X1, self.backpackSlot5Y1)
        pointB = (pointA[0] + self.backpackSlot5W, pointA[1] + self.backpackSlot5H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5ItemType(self):
        pointA = (self.backpackSlot5ItemTypeX1, self.backpackSlot5ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot5ItemTypeW, pointA[1] + self.backpackSlot5ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5ItemAmount(self):
        pointA = (self.backpackSlot5ItemAmountX1, self.backpackSlot5ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot5ItemAmountW, pointA[1] + self.backpackSlot5ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot5ItemBars(self):
        pointA = (self.backpackSlot5ItemBarsX1, self.backpackSlot5ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot5ItemBarsW, pointA[1] + self.backpackSlot5ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6(self):
        pointA = (self.backpackSlot6X1, self.backpackSlot6Y1)
        pointB = (pointA[0] + self.backpackSlot6W, pointA[1] + self.backpackSlot6H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6ItemType(self):
        pointA = (self.backpackSlot6ItemTypeX1, self.backpackSlot6ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot6ItemTypeW, pointA[1] + self.backpackSlot6ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6ItemAmount(self):
        pointA = (self.backpackSlot6ItemAmountX1, self.backpackSlot6ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot6ItemAmountW, pointA[1] + self.backpackSlot6ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot6ItemBars(self):
        pointA = (self.backpackSlot6ItemBarsX1, self.backpackSlot6ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot6ItemBarsW, pointA[1] + self.backpackSlot6ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7(self):
        pointA = (self.backpackSlot7X1, self.backpackSlot7Y1)
        pointB = (pointA[0] + self.backpackSlot7W, pointA[1] + self.backpackSlot7H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7ItemType(self):
        pointA = (self.backpackSlot7ItemTypeX1, self.backpackSlot7ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot7ItemTypeW, pointA[1] + self.backpackSlot7ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7ItemAmount(self):
        pointA = (self.backpackSlot7ItemAmountX1, self.backpackSlot7ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot7ItemAmountW, pointA[1] + self.backpackSlot7ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot7ItemBars(self):
        pointA = (self.backpackSlot7ItemBarsX1, self.backpackSlot7ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot7ItemBarsW, pointA[1] + self.backpackSlot7ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8(self):
        pointA = (self.backpackSlot8X1, self.backpackSlot8Y1)
        pointB = (pointA[0] + self.backpackSlot8W, pointA[1] + self.backpackSlot8H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8ItemType(self):
        pointA = (self.backpackSlot8ItemTypeX1, self.backpackSlot8ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot8ItemTypeW, pointA[1] + self.backpackSlot8ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8ItemAmount(self):
        pointA = (self.backpackSlot8ItemAmountX1, self.backpackSlot8ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot8ItemAmountW, pointA[1] + self.backpackSlot8ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot8ItemBars(self):
        pointA = (self.backpackSlot8ItemBarsX1, self.backpackSlot8ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot8ItemBarsW, pointA[1] + self.backpackSlot8ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9(self):
        pointA = (self.backpackSlot9X1, self.backpackSlot9Y1)
        pointB = (pointA[0] + self.backpackSlot9W, pointA[1] + self.backpackSlot9H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9ItemType(self):
        pointA = (self.backpackSlot9ItemTypeX1, self.backpackSlot9ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot9ItemTypeW, pointA[1] + self.backpackSlot9ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9ItemAmount(self):
        pointA = (self.backpackSlot9ItemAmountX1, self.backpackSlot9ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot9ItemAmountW, pointA[1] + self.backpackSlot9ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot9ItemBars(self):
        pointA = (self.backpackSlot9ItemBarsX1, self.backpackSlot9ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot9ItemBarsW, pointA[1] + self.backpackSlot9ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10(self):
        pointA = (self.backpackSlot10X1, self.backpackSlot10Y1)
        pointB = (pointA[0] + self.backpackSlot10W, pointA[1] + self.backpackSlot10H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10ItemType(self):
        pointA = (self.backpackSlot10ItemTypeX1, self.backpackSlot10ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot10ItemTypeW, pointA[1] + self.backpackSlot10ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10ItemAmount(self):
        pointA = (self.backpackSlot10ItemAmountX1, self.backpackSlot10ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot10ItemAmountW, pointA[1] + self.backpackSlot10ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot10ItemBars(self):
        pointA = (self.backpackSlot10ItemBarsX1, self.backpackSlot10ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot10ItemBarsW, pointA[1] + self.backpackSlot10ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11(self):
        pointA = (self.backpackSlot11X1, self.backpackSlot11Y1)
        pointB = (pointA[0] + self.backpackSlot11W, pointA[1] + self.backpackSlot11H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11ItemType(self):
        pointA = (self.backpackSlot11ItemTypeX1, self.backpackSlot11ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot11ItemTypeW, pointA[1] + self.backpackSlot11ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11ItemAmount(self):
        pointA = (self.backpackSlot11ItemAmountX1, self.backpackSlot11ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot11ItemAmountW, pointA[1] + self.backpackSlot11ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot11ItemBars(self):
        pointA = (self.backpackSlot11ItemBarsX1, self.backpackSlot11ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot11ItemBarsW, pointA[1] + self.backpackSlot11ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12(self):
        pointA = (self.backpackSlot12X1, self.backpackSlot12Y1)
        pointB = (pointA[0] + self.backpackSlot12W, pointA[1] + self.backpackSlot12H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12ItemType(self):
        pointA = (self.backpackSlot12ItemTypeX1, self.backpackSlot12ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot12ItemTypeW, pointA[1] + self.backpackSlot12ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12ItemAmount(self):
        pointA = (self.backpackSlot12ItemAmountX1, self.backpackSlot12ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot12ItemAmountW, pointA[1] + self.backpackSlot12ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot12ItemBars(self):
        pointA = (self.backpackSlot12ItemBarsX1, self.backpackSlot12ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot12ItemBarsW, pointA[1] + self.backpackSlot12ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13(self):
        pointA = (self.backpackSlot13X1, self.backpackSlot13Y1)
        pointB = (pointA[0] + self.backpackSlot13W, pointA[1] + self.backpackSlot13H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13ItemType(self):
        pointA = (self.backpackSlot13ItemTypeX1, self.backpackSlot13ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot13ItemTypeW, pointA[1] + self.backpackSlot13ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13ItemAmount(self):
        pointA = (self.backpackSlot13ItemAmountX1, self.backpackSlot13ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot13ItemAmountW, pointA[1] + self.backpackSlot13ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot13ItemBars(self):
        pointA = (self.backpackSlot13ItemBarsX1, self.backpackSlot13ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot13ItemBarsW, pointA[1] + self.backpackSlot13ItemBarsH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14(self):
        pointA = (self.backpackSlot14X1, self.backpackSlot14Y1)
        pointB = (pointA[0] + self.backpackSlot14W, pointA[1] + self.backpackSlot14H)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14ItemType(self):
        pointA = (self.backpackSlot14ItemTypeX1, self.backpackSlot14ItemTypeY1)
        pointB = (pointA[0] + self.backpackSlot14ItemTypeW, pointA[1] + self.backpackSlot14ItemTypeH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14ItemAmount(self):
        pointA = (self.backpackSlot14ItemAmountX1, self.backpackSlot14ItemAmountY1)
        pointB = (pointA[0] + self.backpackSlot14ItemAmountW, pointA[1] + self.backpackSlot14ItemAmountH)
        cv2.rectangle(self.image, pointA, pointB, self.regionColor, self.regionThickness)

    def drawRegionBackpackSlot14ItemBars(self):
        pointA = (self.backpackSlot14ItemBarsX1, self.backpackSlot14ItemBarsY1)
        pointB = (pointA[0] + self.backpackSlot14ItemBarsW, pointA[1] + self.backpackSlot14ItemBarsH)
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

    def drawRegionShieldBar(self):
        pointA = (self.shieldBarX1, self.shieldBarY1)
        pointB = (pointA[0] + self.shieldBarW, pointA[1] + self.shieldBarH)
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

    def drawRegionAbilityPercentText(self):
        pointA = (self.abilityPercentTextX1, self.abilityPercentTextY1)
        pointB = (pointA[0] + self.abilityPercentTextW, pointA[1] + self.abilityPercentTextH)
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
            confidenceLevel += 2
        if(weapon2TextSimilarity >= .80):
            confidenceLevel += 2
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

    def getHealthAmount(self):
        pointA = (self.healthBarX1, self.healthBarY1)
        pointB = (pointA[0] + self.healthBarW, pointA[1] + self.healthBarH)
        healthBarImage = self.image[pointA[1]:pointB[1], pointA[0]:pointB[0]]
        grayHealthBarImage = cv2.cvtColor(healthBarImage, cv2.COLOR_BGR2GRAY)
        binaryHealthBarImage = cv2.threshold(grayHealthBarImage, 200, 255, cv2.THRESH_BINARY)[1]

        # cv2.imwrite("../output/healthBar.jpg", healthBarImage)
        # cv2.imwrite("../output/grayHealthBar.jpg", grayHealthBarImage)
        # cv2.imwrite("../output/binaryHealthBar.jpg", binaryHealthBarImage)

        count = 0
        for x in range(0, 238):
            if binaryHealthBarImage[8][x] == 255:
                count += 1

        return round(count/238, 2) * 100
