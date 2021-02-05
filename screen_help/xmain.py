from pyautogui import *
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
import keyboard
import win32con
import win32api
import win32gui
import threading
import msvcrt
import sys
from random import randint, random, choice, choices, sample, shuffle
from time import sleep, time
from PIL import Image, ImageDraw
import mouse
import ast

dc = win32gui.GetDC(0)

x_int = 256
y_int = 512

# mass = []
# xxyy = []
# for i in range(32):
# 	xx = i*8
# 	for ii in range(32):
# 		yy = ii*8
# 		xy = []
# 		for x in range(8):
# 			for y in range(8):
# 				xy.append([x_int + xx + x, y_int + yy + y])
# 		xxyy.append(xy)
#
#
# while True:
# 	# z =
# 	greb = choices(xxyy, k=256)
# 	for i in greb:
# 		for xy in i:
# 			win32gui.SetPixel(dc, xy[0], xy[1], win32api.RGB(0, 0, 255))
#
# 	sleep(3)
#
# 	for i in xxyy:
# 		for xy in i:
# 			win32gui.SetPixel(dc, xy[0], xy[1], win32api.RGB(0, 0, 0))


def led_hor():  # --
	mass = []
	for i in range(39):
		mass.append([1 + i, 0])
	for i in range(41):
		mass.append([i, 1])
	for i in range(39):
		mass.append([1 + i, 2])

	return mass


def led_ver():  # |
	mass = []
	for i in range(39):
		mass.append([0, 1+i])
	for i in range(41):
		mass.append([1, i])
	for i in range(39):
		mass.append([2, 1+i])

	return mass


def led_dia1():  # \
	mass = []
	mass_y = []
	for i in range(41):
		mass_y.append(i)

	for n, x in enumerate(range(40)):
		for i in range(-2, 3):
			if mass_y[n]+i >= 40:
				continue
			if mass_y[n]+i < 0:
				continue
			mass.append([x,  mass_y[n]+i])

	return mass


def led_dia2():  # /
	mass = []
	mass_y = []
	for i in range(40, -1, -1):
		mass_y.append(i)

	for n, x in enumerate(range(40)):
		for i in range(-3, 2):
			if mass_y[n]+i >= 40:
				continue
			if mass_y[n]+i < 0:
				continue
			mass.append([x,  mass_y[n]+i])

	return mass


mass = []

for i in led_hor():
	if i in mass:
		continue
	else:
		mass.append(i)

for i in led_ver():
	if i in mass:
		continue
	else:
		mass.append(i)

for i in led_dia1():
	if i in mass:
		continue
	else:
		mass.append(i)

for i in led_dia2():
	if i in mass:
		continue
	else:
		mass.append(i)


while True:
	x_int = 256+120
	y_int = 400
	for i in range(3):
		for ii in led_ver():
			win32gui.SetPixel(dc, ii[0] + x_int, ii[1] + y_int, win32api.RGB(255, 0, 0))
		y_int += 40

	for i in range(3):
		x_int -= 40
		for ii in led_hor():
			win32gui.SetPixel(dc, ii[0] + x_int, ii[1] + y_int, win32api.RGB(255, 0, 0))

	x_int = 256
	y_int = 400

	for x in range(3):
		for y in range(3):
			for i in mass:
				win32gui.SetPixel(dc, i[0] + x_int, i[1] + y_int, win32api.RGB(255, 0, 0))
			x_int += 40
		y_int += 40
		x_int = 256












