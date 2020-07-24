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
        self.point2 = Point(graphX + 12, graphY - 12)
        self.rect = Rectangle(self.point1, self.point2)

    def setColor(self, color):
        if color > 255:
            color = 255
        self.rect.setFill(color_rgb(int(color * .5), color, int(color * .75)))

    def drawRect(self, win):
        self.rect.draw(win)

    def setCrit(self, value):
        self.crit = value

    def colorCrit(self):
        if self.crit > .99:
            self.crit = .99
        self.rect.setFill(color_rgb(int(self.crit*255), 0, int((self.crit*255)*.75)))
