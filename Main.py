######################################################################
# A graphical representation of the Olami Feder Christensen Model.
# All code below is written by Rusty Dotson
######################################################################
import random
from Node import *


def create_grid():
    """
    Creates and returns a 2d list of nodes to present the Olami model
    :return: grid
    """
    grid = []
    gridWidth = 25
    gridHeight = 25
    for y in range(gridHeight):
        row = []
        for x in range(gridWidth):
            newNode = Node(.2, x, y - 10, x * 25, (y * 25)-10)
            newNode.setColor(int(newNode.crit * 255))
            row.append(newNode)
        grid.append(row)
    return grid


def iterateGrid():
    falloffValue = .05
    while True:
        for row in grid:
            for point in row:
                if point.crit > 1:
                    if point.posY == 0 and point.posX == 0:
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + falloffValue

                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()


                    elif point.posY == 0 and point.posX == len(grid[0]) - 1:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + falloffValue

                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()


                    elif point.posY == len(grid) - 1 and point.posX == 0:
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + falloffValue

                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()

                    elif point.posY == len(grid) - 1 and point.posX == len(grid[0]) - 1:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + falloffValue

                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()


                    elif point.posY == len(grid) - 1:
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + falloffValue
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + falloffValue

                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()
                        grid[point.posX - 1][point.posY].colorCrit()


                    elif point.posX == 0:
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + falloffValue
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + falloffValue

                        grid[point.posX][point.posY + 1].colorCrit()
                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()


                    elif point.posX == len(grid[0]) - 1:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + falloffValue
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + falloffValue

                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()


                    elif point.posY == 0:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + falloffValue
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + falloffValue

                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()


                    else:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + falloffValue
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + falloffValue
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + falloffValue
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + falloffValue
                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()

                    point.setCrit(.05)

            rand1 = random.randrange(0, 25)
            rand2 = random.randrange(0, 25)
            point = grid[rand1][rand2]
            if point.crit < 1:
                point.setCrit(point.crit + .008)
            point.setColor(int((point.crit + .05) * 255))


def print_grid():
    """
    Prints a graphical representation of all nodes used for the model.
    :param grid:
    :param win:
    :return: None
    """
    for row in grid:
        for node in row:
            node.drawRect(win)
    print(len(grid))


win = GraphWin("SPFFH", 561, 566)
win.setBackground(color_rgb(10, 10, 10))
grid = create_grid()
print_grid()


def main():
    iterateGrid()
    win.getMouse()
    win.close()


main()
