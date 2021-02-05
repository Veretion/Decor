from PIL import Image, ImageDraw
from random import choice

size_x = 255*5
size_y = 64

image = Image.new('RGB', (size_x, size_y))
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

a = 255
b = 0
c = 0

v0 = 0
v1 = 0
v2 = 0
v3 = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0

for x in range(width):
	for y in range(height):
		draw.point((x, y), (a, b, c))
	# if v1 == 0 and b > 0 and c > 0:
	# 	v0 = 1
	# 	b -= 1
	# 	c -= 1
	if v2 == 0 and b < 254:
		v1 = 1
		b += 1
	elif v3 == 0 and a > 0:
		v2 = 1
		a -= 1
	elif v4 == 0 and c < 254:
		v3 = 1
		c += 1
	elif v5 == 0 and b > 0:
		v4 = 1
		b -= 1
	elif v6 == 0 and a < 254:
		v5 = 1
		a += 1
	# elif v7 == 0 and a > 0:
	# 	v6 = 1
	# 	a -= 1
	# 	c -= 1

image.save("karta_cv_rgb10.png", "PNG")




