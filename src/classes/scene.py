import cv2
from frame import Frame

class Scene:
    frame
    subImages = {}
    extractedData = {}

    # scene list:
    # - main menu
    # - lobby
    # - - level
    # - - username
    # - - mic enabled
    # - - crafting metal count
    # - - legend token count
    # - - apex coin count
    # - - gamemode selected
    # - - ready status
    # - - friends online
    # - match summary
    # - - squad placed
    # - - squad placed out of
    # - - played #h #m ago
    # - - time survived
    # - - kill count
    # - - damage done
    # - - revive ally count
    # - - respawn ally count
    # - - killed champion count
    # - - kill leader count
    # - - playing with friends count
    # - - total xp earned
    # - - current level
    # - - current xp level
    # - - next level xp
    # - - next level
    # - - next reward
    # - - battle pass total earned match xp
    # - - battle pass playing with friends
    # - - battle pass legend bonus
    # - - total earned battle pass points
    # - - current battle pass level
    # - - current battle pass xp
    # - - next battle pass level xp
    # - - next battle pass level
    # - - next battle pass reward
    # - black fade transition
    # - legendSelect
    # - legendTeamOverview
    # - championTeamOverview
    # - drop ship
    # - gameplay (consisting of the following states):
    # - - inventory open
    # - - ping wheel open
    # - - health wheel open
    # - - ordnance wheel open
    # - - map open
    # - - hit target

    def __init__(self, frame):
        self.frame = frame

        self.determineIfInMenu
