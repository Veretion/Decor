from PIL import Image, ImageDraw
from time import time


path = "E:\\Photo_rad\\"
Fname = 'photo100718.png'


pt1 = [42, 198]  # точка начала экрана левый верхний
pt2 = [771, 198]  # точка конца экрана правый верхний

pt3 = 0  # 0 если не используется, правый нижний угол
pt4 = 0  # 0 если не используется, левый нижний угол

height_rad = 55  # высота от пола в пикселях
points = [pt1, pt2, pt3, pt4, height_rad]

ost = 5  # оступ в пикселях по сторонам

color = (32, 27, 28)


# Fname = 'x2.png'
#
# pt1 = [422, 182]  # точка начала экрана левый верхний
# pt2 = [966, 192]  # точка конца экрана правый верхний
#
# pt3 = 0  # 0 если не используется, правый нижний угол
# pt4 = 0  # 0 если не используется, левый нижний угол
#
# height_rad = 85  # высота от пола в пикселях
# points = [pt1, pt2, pt3, pt4, height_rad]
#
# ost = 5  # оступ в пикселях по сторонам
#
# color = (48, 12, 8)


path = path + Fname

image = Image.open(path)  # Открываем изображение
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
width = image.size[0]  # Определяем ширину
height = image.size[1]  # Определяем высоту
pix = image.load()  # Выгружаем значения пикселей

# Start код


def fig_kvad(left, up, right, down, ost):
	mass = []

	left += ost
	up += ost
	right -= ost
	down -= ost

	# рисунок
	ad = []

	iscl = []  #

	for i in range(15):
		for ii in range(15):
			if [i, ii] not in iscl:
				ad.append([i, ii])

	a = 0  # размер фигуры по x
	b = 0  # размер фигуры по y
	# рисунок

	b0 = 0

	for x in range(right - left):
		a0 = 0
		for y in range(down - up):

			if [a0, b0] in ad:
				mass.append([left + x, up + y])
			a0 += 1
			if a0 > a:
				a0 = 0
		b0 += 1
		if b0 > b:
			b0 = 0

	return mass


def fig_kub(left, up, right, down, ost):
	mass = []

	left += ost
	up += ost
	right -= ost
	down -= ost

# рисунок
	# исключения
	iscl = [[0, 0], [1, 0], [2, 0], [3, 0]
			, [0, 1], [1, 1], [2, 1]
			, [0, 2], [1, 2]
			, [0, 3]]
	iscl += [ [11, 0], [12, 0], [13, 0], [14, 0]
			 ,         [12, 1], [13, 1], [14, 1]
			 ,[                  13, 2], [14, 2]
			 ,                           [14, 3]]
	iscl += [[0,14], [1,14], [2,14], [3,14],
			 [0, 13],[1,13], [2,13],
			 [0, 12],[1,12],
			 [0, 11],

			 ]
	iscl += [[14, 11],
			 [14, 12], [13, 12],
			 [14, 13], [13, 13], [12, 14],
			 [14, 14], [13, 14], [12, 14], [11, 14] ]


	ad = []
	for i in range(15):
		for ii in range(15):
			if [i, ii] not in iscl:
				if ii != 7:
					ad.append([i, ii])

	a = 17  # длинна фигуры
	b = 17  # высота фигуры
# рисунок


	b0 = 0

	for x in range(right - left):
		a0 = 0
		for y in range(down - up):

			if [a0, b0] in ad:
				mass.append([left + x, up + y])
			a0 += 1
			if a0 > a:
				a0 = 0
		b0 += 1
		if b0 > b:
			b0 = 0

	return mass


def fig_shest(left, up, right, down, ost):
	mass = []

	left += ost
	up += ost
	right -= ost
	down -= ost

	# рисунок
	ad = []

	iscl = [[0, 0], [0, 1], [1, 0],     # левый верх
			[4, 0], [4, 1], [3, 0],  # правый верх
			[0, 11], [0, 12], [1, 12],  # левый низ
			[4, 11], [4, 12], [3, 12]]  # правый низ

	for x in range(5):
		for y in range(13):
			if [x, y] not in iscl:
				ad.append([x, y])

	b = 10  # x
	a = 16  # y
	# рисунок

	b0 = 0

	for x in range(right - left):
		a0 = 0
		for y in range(down - up):

			if [b0, a0] in ad:
				mass.append([left + x, up + y])
			a0 += 1
			if a0 > a:
				a0 = 0
		b0 += 1
		if b0 > b:
			b0 = 0

	return mass


def fig_plus(left, up, right, down, ost):
	mass = []

	left += ost
	up += ost
	right -= ost
	down -= ost

	# рисунок
	ad = []

	iscl = []  #
	# for i in range(2):
	# 	for ii in range(6):
	# 		if [i, ii] not in iscl and ([i, ii] not in ad):

	for i in range(2, 10):
		for ii in range(2, 4):
				ad.append([i, ii])

	a = 14  # размер фигуры по x
	b = 14  # размер фигуры по y
	# рисунок

	b0 = 0

	for x in range(right - left):
		a0 = 0
		for y in range(down - up):

			if [a0, b0] in ad:
				mass.append([left + x, up + y])
			a0 += 1
			if a0 > a:
				a0 = 0
		b0 += 1
		if b0 > b:
			b0 = 0

	return mass


############################

left = points[0][0]
up = points[0][1]
right = points[1][0]
down = (points[3][1] if points[3] else height - points[4])

print(0)

mass = fig_shest(left, up, right, down, ost)
for x in range(width):
	for y in range(height):
		if x < left or x > right or y < up or y > down:
			mass.append([x, y])
# End код

carts = []
for x in range(width):
	xx = []
	for y in range(height):
		xx.append([(x, y), color])
	carts.append(xx)

for i in mass:
	x = i[0]
	y = i[1]
	carts[x][y] = [(x, y), pix[x, y]]

for x in carts:
	for y in x:
		draw.point(y[0], y[1])


image.save(path.split('.', -1)[0] + '_' + str(time()) + '.png', "JPEG")  # не забываем сохранить изображение
