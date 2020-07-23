######################################################################
# A graphical representation of the Olami Feder Christensen Model.
# All code below is written by Rusty Dotson, but makes use of
# the Graphics library written by John Zelle.
######################################################################
import random
import numpy as np
from graphics import *
from Node import *
import time


def create_grid():
    """
    Creates and returns a 2d list of nodes to present the Olami model
    :return: grid
    """
    grid = []
    gridWidth = 50
    gridHeight = 50
    for y in range(gridHeight):
        row = []
        for x in range(gridWidth):
            newNode = Node(.7, x, y, x * 10, y * 10)
            newNode.setColor(int(newNode.crit * 255))
            row.append(newNode)
        grid.append(row)
    return grid


def olami():
    """
    performs the processes to execute the Olami model.
    :return: None
    """
    stable = True
    while stable:
        rand1 = random.randrange(0, 50)
        rand2 = random.randrange(0, 50)
        point = grid[rand1][rand2]
        if point.crit > .9:
            point.setCrit(.1)
            stable = False
            spread(point)
        else:
            point.setCrit(point.crit + .05)
            point.setColor(int((point.crit + .05) * 255))
    return

def spread(point):
    if point.posY == 0 and point.posX == 0:
        print(1)
        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + .1
        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + .10

    elif point.posY == 0 and point.posX == len(grid[0])-1:
        print(2)
        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + .1
        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + .10

    elif point.posY == len(grid)-1 and point.posX == 0:
        print(3)
        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + .1
        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + .10

    elif point.posY == len(grid)-1 and point.posX == len(grid[0])-1:
        print(4)
        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + .1
        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + .10

    elif point.posY == len(grid)-1:
        print(5)
        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + .1
        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + .10
        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + .10

    elif point.posX == 0:
        print(6)
        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + .1
        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + .1
        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + .10

    elif point.posX == len(grid[0])-1:
        print(7)
        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + .1
        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + .1
        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + .1

    elif point.posY == 0:
        print(8)
        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + .1
        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + .1
        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + .10

    else:
        print(9)
        grid[point.posX - 1][point.posY].crit = grid[point.posX - 1][point.posY].crit + .1
        grid[point.posX + 1][point.posY].crit = grid[point.posX + 1][point.posY].crit + .1
        grid[point.posX][point.posY - 1].crit = grid[point.posX][point.posY - 1].crit + .10
        grid[point.posX][point.posY + 1].crit = grid[point.posX][point.posY + 1].crit + .10

    for row in grid:
        for node in row:
            if node.crit > .9:
                node.setCrit(.1)
                olami()




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


win = GraphWin("my Window", 500, 500)
win.setBackground(color_rgb(0, 0, 0))
grid = create_grid()
print_grid()


def main():
    #win = GraphWin("my Window", 500, 500)
    #win.setBackground(color_rgb(0, 0, 0))
    #grid = create_grid()
    #print_grid(grid, win)
    olami()
    win.getMouse()
    win.close()


main()
