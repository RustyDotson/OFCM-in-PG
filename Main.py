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
    gridHeight = 51
    for y in range(gridHeight):
        row = []
        for x in range(gridWidth):
            newNode = Node(.5, x, y, x * 10, y * 10)
            newNode.setColor(int(newNode.crit * 255))
            row.append(newNode)
        grid.append(row)
    return grid


def olami():
    """
    performs the processes to execute the Olami model.
    :return: None
    """
    return


def print_grid(grid, win):
    """
    Prints a graphical representation of all nodes used for the model.
    :param grid:
    :param win:
    :return: None
    """
    for row in grid:
        for node in row:
            node.drawRect(win)
    while True:
        grid[random.randrange(0, 51)][random.randrange(0, 50)].setColor(int((random.uniform(.01, .99) * 255)))
        time.sleep(.01)


def main():
    win = GraphWin("my Window", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    grid = create_grid()
    print_grid(grid, win)
    win.getMouse()
    win.close()


main()
