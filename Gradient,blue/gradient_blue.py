from PIL import Image, ImageDraw

# size image
size_x = 512
size_y = 512

# direction
horizontal = True  # bool-value
vertical = False  # bool-value

# gradient
invert = False  # bool-value
rotate = 0  # градусов против часовой стрелки

image = Image.new('RGB', (512, 512))
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

for x in range(width):
	for y in range(height):

		# if y < 256 and x < 256:
		# 	draw.point((x, y), (255 - x if y % 2 == 0 else 0, 255 - x if y % 2 == 0 else 0, 255 if y % 2 == 0 else 0,))
		# elif x > 255 > y:
		# 	draw.point((x, y), (x - 256 if y % 2 == 0 else 0, x - 256 if y % 2 == 0 else 0, 0 if y % 2 == 0 else 255))
		#
		# elif x < 255 < y:
		# 	draw.point((x, y), (255 - x if y % 2 == 0 else 0, 255 - x if y % 2 == 0 else 0, 255 if y % 2 == 0 else 0,))
		# else:
		# 	draw.point((x, y), (x - 256 if y % 2 == 0 else 0, x - 256 if y % 2 == 0 else 0, 0 if y % 2 == 0 else 255))

		if horizontal:
			if x < 256:
				# if x < 512:
				draw.point((x, y), (0, 0, x))
				# draw.point((x, y), (round(x/2), round(x/2), round(x/2)))
				# draw.point((x, y), (x, 0, 0))  # red
			else:
				draw.point((x, y), (x - 256, x - 256, 256))
				# draw.point((x, y), (256, x - 256, x - 256))  # red

		if vertical:
			if y < 256:
				draw.point((x, y), (0, 0, y))
			else:
				draw.point((x, y), (y - 256, y - 256, 256))

image = image.rotate(180) if invert else image
image = image.rotate(rotate)
image = image.resize((size_x, size_y), Image.ANTIALIAS)
image.save(str(size_x) + 'x' + str(size_y) + "_blue.png", "PNG")



















