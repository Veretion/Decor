from PIL import Image, ImageDraw
from random import choice

bams = 1000  # квадрат
size_x = bams
size_y = bams

image = Image.new('RGB', (size_x, size_y))
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()


for xn, x in enumerate(range(width)):
	xxn = round((xn/bams) ** (xn/bams), 3)
	for yn, y in enumerate(range(height)):
		# draw.point((x, y), choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]))
		# if int(abs(x ** x)) <= yn:
		if xn == 368:
			draw.point((x, y), (0, 0, 255))
			continue
		if yn/bams < xxn:
			draw.point((x, y), (0, 0, 0))
		else:
			draw.point((x, y), (255, 255, 255))

image = image.transpose(Image.FLIP_TOP_BOTTOM)
image.save("grafic kvad " + str(bams) + " x^x.png", "PNG")




