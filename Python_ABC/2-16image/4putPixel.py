from PIL import Image

im = Image.new('RGBA', (100, 100))
print('transparent background: {}'.format(im.getpixel((0, 0))))

for x in range(100):
	for y in range(50):
		im.putpixel((x, y), (20, 165, 210))
#
from PIL import ImageColor
#
for x in range(100):
	for y in range(50, 100):
		im.putpixel((x, y), ImageColor.getcolor('violet', 'RGBA'))
#
print('upper part: {}'.format(im.getpixel((0, 0))))
print('lower part: {}'.format(im.getpixel((0, 50))))
#
im.save('putPixel.png')