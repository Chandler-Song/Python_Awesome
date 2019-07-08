from PIL import Image

# new image
# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('purpleImage.png')
#
# im2 = Image.new('RGBA', (20, 20))
# im2.save('transparentImage.png')

# crop image and paste
# dollIm = Image.open('doll.jpg')
# #
croppedIm = dollIm.crop((266,71,500,566))
# croppedIm.save('cropped.jpg')
# #
# dollCopyIm = dollIm.copy()
# #
# dollCopyIm.paste(croppedIm, (0,0))
# dollCopyIm.paste(croppedIm, (700,300))
# #
# dollCopyIm.save('pasted.jpg')

# Pasting Transparent Pixels
# reindeerIm = Image.open('reindeer.png')
# dollCopyIm.paste(reindeerIm, (0, 200))
# dollCopyIm.paste(reindeerIm, (500, 50), reindeerIm)
#
# dollCopyIm.save('transparentBackground.jpg')

# tiled balloon
hotAirBalloonIm = Image.open('hotAirBalloon.jpg')

balloonIm = hotAirBalloonIm.crop((627,164,755,322))
balloonIm.save('balloonIm.jpg')

hotAirBalloonImWidth, hotAirBalloonImHeight = hotAirBalloonIm.size
balloonWidth, balloonHeight = balloonIm.size

hotAirBalloonCopy = hotAirBalloonIm.copy()

for left in range(0, hotAirBalloonImWidth, balloonWidth):
	for top in range(0, hotAirBalloonImHeight, balloonHeight):
		hotAirBalloonCopy.paste(balloonIm, (left,top))

hotAirBalloonCopy.save('tiled.jpg')


