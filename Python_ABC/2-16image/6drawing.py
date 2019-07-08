from PIL import Image, ImageDraw

# drawing shapes
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
#
# draw.line([(0,0), (199,0), (199, 199), (0,199), (0,0)], fill='pink', width=10)
# draw.rectangle((20,30,60,60), fill='blue')
# draw.ellipse((120,30,160,60), fill='red')
# draw.polygon(((57,87),(79,62),(94,85),(120,90),(103,113)), fill='brown', outline='green')
# #
# for i in range(100,200,10):
# 	draw.line([(i,0), (200,i-100)], fill='purple')
# im.save('drawing.png')

# drawing text
from PIL import ImageFont

im = Image.new('RGBA', (200,200), 'white')
draw = ImageDraw.Draw(im)

draw.text((20,150), 'Hello', fill='purple')

# fontsFolder = '/Library/Fonts/'
# SignPainterFont = ImageFont.truetype(fontsFolder+'SignPainter.ttc', 32)

SignPainterFont = ImageFont.truetype('SignPainter.ttc', 32)

# On Windows: C:\Windows\Fonts; On OS X: /Library/Fonts

draw.text((100,150), 'Howdy', fill='gray', font=SignPainterFont)
im.save('text.png')


