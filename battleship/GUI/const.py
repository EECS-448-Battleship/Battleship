# This is a file for keeping track of various constants used in the GUI

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
from pygame.locals import *

pg.init()

pygame = pg
width = 1000
height = 600
fps = 30

fill_color = (66, 123, 181)
text_color = (255, 255, 255)
text_bkg_color = (29, 58, 87)
button_bkg_color = (21, 43, 64)

clock = pygame.time.Clock()
