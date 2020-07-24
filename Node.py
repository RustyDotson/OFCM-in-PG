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
        if color > 255:
            color = 255
        #self.rect.setFill(color_rgb(int(color * .5), color, int(color * .75)))
        #self.rect.setFill(color_rgb(int(color), 0, int(color * .75)))
        if self.crit > 1:
            self.rect.setFill(color_rgb(color, 0, 0))
        elif self.crit > .7:
            self.rect.setFill(color_rgb(color, int(color * .64), 0))
        elif self.crit > .4:
            self.rect.setFill(color_rgb(color, color, 0))
        else:
            self.rect.setFill(color_rgb(0, color, 0))



    def drawRect(self, win):
        self.rect.draw(win)

    def setCrit(self, value):
        self.crit = value

    def colorCrit(self):
        print(self.crit)
        if self.crit > .99:
            self.crit = .99
        if self.crit > 1:
            self.rect.setFill(color_rgb(int(self.crit*255), 0, 0))
        elif self.crit > .7:
            self.rect.setFill(color_rgb(int(self.crit*255), int((self.crit*255)*.64), 0))
        elif self.crit > .4:
            self.rect.setFill(color_rgb(int(self.crit*255), int(self.crit*255), 0))
        else:
            self.rect.setFill(color_rgb(0, int(self.crit * 255), 0))
