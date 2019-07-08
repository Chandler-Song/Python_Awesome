from PIL import Image

ArwenIm = Image.open('Arwen.jpg')

# resize an image
# print(ArwenIm.size)

width, height = ArwenIm.size

quartersizedIm = ArwenIm.resize((int(width/2), int(height/2)))
# quartersizedIm.save('ArwenQuartersized.jpg')
# print(quartersizedIm.size)
#
# sveltIm = ArwenIm.resize((width, height+200))
# sveltIm.save('ArwenSvelte.jpg')

# rotate an image
ArwenIm.rotate(90).save('ArwenRotated90.jpg')
# ArwenIm.rotate(180).save('ArwenRotated180.jpg')
# ArwenIm.rotate(270).save('ArwenRotated270.jpg')

# expand=True keyword argument
# ArwenIm.rotate(10).save('ArwenRotated10.jpg')
# ArwenIm.rotate(10, expand=True).save('ArwenRotated10_extend.jpg')

# mirror flip
ThranduilIm = Image.open('thranduil.jpg')
#
ThranduilIm.transpose(Image.FLIP_LEFT_RIGHT).save('ThranduilHorizontal_flip.jpg')
# ThranduilIm.transpose(Image.FLIP_TOP_BOTTOM).save('ThranduilVertical_flip.jpg')
# ThranduilIm.rotate(180).save('ThranduilRotated180.jpg')

