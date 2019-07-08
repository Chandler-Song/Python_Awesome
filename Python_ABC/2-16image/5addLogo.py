# # addLogo.py - Add logo to the lower-right corner.
#
from pathlib import Path
from PIL import Image
#
# # image folder
PATH = '/Users/Smonkey/Documents/Python/PythonABC_Online/2-16image/toAddLogo/'
LOGOFILENAME = 'transparentLogo.png'
#
# # function to resize big logo image
def resizeLogo(p):
#
    originalLogoIm = Image.open(str(p))
    w, h = originalLogoIm.size
#
    nWidth, nHeight = int(w/3), int(h/3)
#
#     # nFilename: path of smallLogo.pnp
    nFilename = str(p.parent/'withLogo'/'smallLogo.png')
#
    originalLogoIm.resize((nWidth, nHeight)).save(nFilename)
#
    return nWidth, nHeight, nFilename
#
# # set up new folder for image with logo
imagePath = Path(PATH)
#
# # setup new folder 'withLogo'
imageWithLogoFolder = imagePath.joinpath('withLogo')
imageWithLogoFolder.mkdir(777, exist_ok=True,)
#
# # resize big logo image
logoWidth, logoHeight, logo = resizeLogo(imagePath/LOGOFILENAME)
#
logoIm = Image.open(logo)
#
# # Loop over all files in the working directory.
for fname in imagePath.iterdir():
# for fname in [x for x in imagePath.iterdir() if x.is_file]:
    filename = fname.name
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGOFILENAME:
        continue # skip non-image files
#
    imageLocation = PATH + filename
    im = Image.open(imageLocation)
    width, height = im.size
#
    # Add logo.
    print('Adding logo to {}...'.format(filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
#
    # Save changes.
    im.save(str(imagePath.joinpath('withLogo').joinpath(filename)))
#
Path(logo).unlink()
