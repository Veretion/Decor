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
from random import randint, random, choice
from time import sleep, time
from PIL import Image, ImageDraw
import mouse
import ast
import os

# print(os.listdir('C:'))


def otrisov(mass):

	dc = win32gui.GetDC(0)
	blued = win32api.RGB(0, 0, 255)
	reded = win32api.RGB(255, 0, 0)

	def blue(x, y):
		win32gui.SetPixel(dc, x, y, blued)

	def red(x, y):
		win32gui.SetPixel(dc, x, y, reded)

	for _ in range(1):
		sleep(0.01)
		# xx = 1024
		xx = 640
		yy = 512

		for i in mass:
			red(xx + i[0], yy + i[1])


def krug(a):
	# a - радиус круга минимум 3
	x = 0
	y = a
	mass = []
	while True:
		x = round(x)
		y = round(y)

		if [x, y] not in mass:
			mass.append([x, y])
			mass.append([-x, y])
			mass.append([x, -y])
			mass.append([-x, -y])

		if x <= round(((a ** 2) / 2) ** 0.5):
			x += 1
			y = (a ** 2 - x ** 2) ** 0.5

		elif x >= round(((a ** 2) / 2) ** 0.5) and y >= 0:
			y -= 1
			x = (a ** 2 - y ** 2) ** 0.5
		else:
			break

	return mass


# отображение на экране
# while True:
# 	for i in range(10, 500, 3):
# 		otrisov(krug(i))


# запись в файл
from PIL import Image, ImageDraw

radius = 0
# создаёт фото и рисует в цецнтре
# один
# radius = 250
# или несколько кругов

n = [i for i in range(3, 4200, 3)]


size_x = 9000
size_y = 9000

image = Image.new('RGB', (size_x, size_y), (255, 255, 255))
draw = ImageDraw.Draw(image)
half_size_x = size_x/2
half_size_y = size_y/2

if radius:
	mass = krug(radius)
else:
	mass = []
	for i in n:
		mass = krug(i)
		for i in mass:
			x = i[0] + half_size_x
			y = i[1] + half_size_y
			draw.point((x, y), (0, 0, 0))

image.save("krug.png", "PNG")















