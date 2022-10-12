"""
Tutorial: https://www.youtube.com/watch?v=-LsuiVGO-88&list=TLPQMDMxMDIwMjIPzkQwxDNm1Q&index=4
Requirements:
    numpy==1.23.3
    opencv-python==4.6.0.66
"""

import numpy as np
import cv2 as cv
import random

# general parameters
width = 900
height = 600
n_trees = 30
ground_level = height-100

# blank image
bg = np.zeros((height, width, 3), dtype=np.uint8)

# draw background
cv.rectangle(bg,(width,0), (0, ground_level), (255,225,95), -1)

# *************
class Tree:
    def __init__(self, image):
        self.img = image
        self.loc = int(np.random.choice(range(900), 1))
        self.ht = int(np.random.choice(range(200, 350), 1))
        self.radius = 50
        self.scale = np.random.choice(np.linspace(0.5, 2, num=8), 1)

    def generate_colors(self):
        green = (0, random.randint(130,200) ,0)
        light_green = (35, random.randint(200,250) ,35)
        brown = random.choice([(2, 30, 85), (5, 55, 120), (0,70,140)])
        return green, light_green, brown

    def draw(self):
        small_radius = int((self.radius-20)*self.scale)
        green, light_green, brown = self.generate_colors()

        # leafs
        cv.circle(self.img, (self.loc, ground_level-self.ht), int(self.radius*self.scale), green, -1)
        cv.circle(self.img, (self.loc-int(45*self.scale), ground_level-self.ht+small_radius), small_radius, green, -1)
        cv.circle(self.img, (self.loc+int(45*self.scale), ground_level-self.ht+small_radius), small_radius, green, -1)

        # trunk
        cv.line(self.img, (self.loc, ground_level), (self.loc, ground_level-self.ht), brown, int(20*self.scale))
        cv.line(self.img, (self.loc, ground_level-self.ht+int(75*self.scale)), (self.loc-int(45*self.scale), ground_level-self.ht+small_radius), brown, int(5*self.scale))
        cv.line(self.img, (self.loc, ground_level-self.ht+int(75*self.scale)), (self.loc+int(45*self.scale), ground_level-self.ht+small_radius), brown, int(5*self.scale))

        # leaf highlights
        cv.circle(self.img, (self.loc, ground_level-self.ht), int(self.radius*self.scale-10*self.scale), light_green, -1)
        cv.circle(self.img, (self.loc-int(45*self.scale), ground_level-self.ht+small_radius), small_radius-int(10*self.scale), light_green, -1)
        cv.circle(self.img, (self.loc+int(45*self.scale), ground_level-self.ht+small_radius), small_radius-int(10*self.scale), light_green, -1)

        cv.rectangle(bg,(width, ground_level), (0, height), (70,180,75), -1)
        return self.img
# *************

#display image
for idx in range(n_trees):
    img = Tree(bg).draw()
cv.imshow('forest of objects', img) 

cv.waitKey(0)
cv.destroyAllWindows()