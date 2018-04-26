from src.initialization import *
from src.cheats import *
from src.keyhandling import *
from src.win import *


class Game:
    __instance = None
    def __new__(cls, val):
        if Game.__instance is None:
            Game.__instance = object.__new__(cls)
            Game.__instance.val = val
        return Game.__instance

    #game settings
    h, w, b = 0, 0, 0

    #images, loaded in loadImages() function
    emptyTile, bombTile, pbombTile, flagTile, qmarkTile, cheatTile, nearbyTile = 0, 0, 0, 0, 0, 0, 0

    #tkinter objects
    tileField, flagInfo, buttons = 0, 0, 0

    #lists
    userField, gameField, cheatCode = 0, 0, [0, 0, 0, 0, 0]

    #others
    bombs, cheatIterator, generated, enabledCheat = 0, 0, False, False

    checkParameters = checkParameters #first
    cheat = cheat
    loadImages = loadImages
    generateTiles = generateTiles
    generateLists = generateLists
    findNeighbours = findNeighbours
    leftClickLambda = leftClickLambda
    rightClickLambda = rightClickLambda
    leftClick = leftClick
    rightClick = rightClick
    checkEmptyNeigbours = checkEmptyNeigbours
    checkForWin = checkForWin
    checkForWin2 = checkForWin2









