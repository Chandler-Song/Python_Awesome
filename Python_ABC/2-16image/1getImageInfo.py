from PIL import ImageColor

# Get image color
# print('Red: {}'.format(ImageColor.getcolor('red', 'RGBA')))
# print('RED: {}'.format(ImageColor.getcolor('RED', 'RGBA')))
# #
# print('Black: {}'.format(ImageColor.getcolor('Black', 'RGBA')))
# #
# print('chocolate: {}'.format(ImageColor.getcolor('chocolate', 'RGBA')))
# print('CornflowerBlue: {}'.format(ImageColor.getcolor('CornflowerBlue', 'RGBA')))
# #
# print('Pink: {}'.format(ImageColor.getcolor('Pink', 'RGBA')))

# RGB color decimal code
# https://www.rapidtables.com/web/color/RGB_Color.html

from PIL import Image

# Get image data
dollIm = Image.open('doll.jpg')

print('Size: {}'.format(dollIm.size))
width, height = dollIm.size
print('Width: {}\nHeight: {}'.format(width, height))
#
print('Filename: {}'.format(dollIm.filename))
#
print('Format: {}'.format(dollIm.format))
#
print('Description: {}'.format(dollIm.format_description))
#
dollIm.save('doll_duplicate.png')
