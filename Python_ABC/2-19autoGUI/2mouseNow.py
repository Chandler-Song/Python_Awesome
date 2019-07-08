# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui
import time

print('Press fn+command+F2(Mac) or Ctrl+C(windows) to quit.')
positionStr = ''
try:
    while True:

        time.sleep(3)

        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr = 'X: {:4};  Y: {:4}; RGB:{}'.format(x, y, pixelColor)

        print(positionStr)

except KeyboardInterrupt:
    print('\nDone.')


