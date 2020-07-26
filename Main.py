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
            newNode = Node(.2, x, y, (x * 20) + 5, (y * 20) + 20)
            newNode.setColor(int(newNode.crit * 255))
            row.append(newNode)
        grid.append(row)
    return grid


def iterateGrid():
    """
    Infinitely traverses through the grid. Node's crit values are randomly incremented. When a node is
    critical (critValue reaches 1), their value is then dropped and the surrounding nodes' critValues are then
    incremented by the falloffValue declared at the beginning of the function. This creates an "avalanche" effect that
    you may see when the program runs.
    """
    falloffValue = .2
    while True:
        for row in grid:
            for point in row:
                if point.crit >= .99:
                    if point.posY == 0 and point.posX == 0:
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + (falloffValue * 2)
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + (falloffValue * 2)

                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()


                    elif point.posY == 0 and point.posX == len(grid[0]) - 1:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + (falloffValue * 2)
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + (falloffValue * 2)

                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()


                    elif point.posY == len(grid) - 1 and point.posX == 0:
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + (falloffValue * 2)
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit +(falloffValue * 2)

                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()

                    elif point.posY == len(grid) - 1 and point.posX == len(grid[0]) - 1:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + (falloffValue * 2)
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + (falloffValue * 2)

                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()

                    elif point.posY == len(grid) - 1:
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + (falloffValue * 1.33)
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + (falloffValue * 1.33)
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + (falloffValue * 1.33)

                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()
                        grid[point.posX - 1][point.posY].colorCrit()

                    elif point.posX == 0:
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + (falloffValue * 1.33)
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + (falloffValue * 1.33)
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + (falloffValue * 1.33)

                        grid[point.posX][point.posY + 1].colorCrit()
                        grid[point.posX + 1][point.posY].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()

                    elif point.posX == len(grid[0]) - 1:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + (falloffValue * 1.33)
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + (falloffValue * 1.33)
                        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + (falloffValue * 1.33)

                        grid[point.posX - 1][point.posY].colorCrit()
                        grid[point.posX][point.posY + 1].colorCrit()
                        grid[point.posX][point.posY - 1].colorCrit()

                    elif point.posY == 0:
                        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + (falloffValue * 1.33)
                        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + (falloffValue * 1.33)
                        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + (falloffValue * 1.33)

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

                    point.setCrit(.2)

            rand1 = random.randrange(0, 25)
            rand2 = random.randrange(0, 25)
            point = grid[rand1][rand2]
            #point = grid[12][12]
            if point.crit < 1:
                point.setCrit(point.crit + .03)
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

win = GraphWin("SPFFH", 505, 505)
win.setBackground(color_rgb(10, 10, 10))
grid = create_grid()
print_grid()


def main():
    iterateGrid()
    win.getMouse()
    win.close()


main()
