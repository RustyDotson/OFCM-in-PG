############################################################
# This Node file was entirely coded by Rusty Dotson, but
# imports the graphics library written by John Zelle
############################################################

from graphics import *


class Node:

    def __init__(self, critValue, x, y, graphX, graphY):
        self.crit = critValue
        self.posX = x
        self.posY = y
        self.point1 = Point(graphX, graphY)
        self.point2 = Point(graphX + 10, graphY - 10)
        self.rect = Rectangle(self.point1, self.point2)

    def setColor(self, color):
        self.rect.setFill(color_rgb(0, 0, color))

    def drawRect(self, win):
        self.rect.draw(win)

    def setCrit(self, value):
        self.crit = value

    def colorCrit(self):
        if self.crit > .99:
            self.crit = .99
        self.rect.setFill(color_rgb(0, 0, int(self.crit*255)))
