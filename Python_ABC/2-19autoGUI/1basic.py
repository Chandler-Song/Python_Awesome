import pyautogui, time

#  screen’s width and height in pixels
# print(pyautogui.size())
# width, height = pyautogui.size()
# print(pyautogui.position())

# Moving the Mouse
# for i in range(10):
#       pyautogui.moveTo(100, 100, duration=0.25)
#       pyautogui.moveTo(200, 100, duration=0.25)
#       pyautogui.moveTo(200, 200, duration=0.25)
#       pyautogui.moveTo(100, 200, duration=0.25)

# for i in range(10):
#       pyautogui.moveTo(100, 100)
#       pyautogui.moveTo(200, 100)
#       pyautogui.moveTo(200, 200)
#       pyautogui.moveTo(100, 200)

# time.sleep(2)
# for i in range(10):
#       pyautogui.moveRel(100, 0, duration=0.25)
#       pyautogui.moveRel(0, 100, duration=0.25)
#       pyautogui.moveRel(-100, 0, duration=0.25)
#       pyautogui.moveRel(0, -100, duration=0.25)

# Getting the Mouse Position
# time.sleep(1)
# print(pyautogui.position())

# Click the mouse

# Dragging the mouse

# https://www.sumopaint.com/paint/
#
# time.sleep(2)
# pyautogui.click()    # click to put drawing program in focus
# distance = 200
# interval = 10
# dur = 0.1
#
# # Dragging the Mouse
#
# while distance > 0:
#     pyautogui.dragRel(distance, 0, dur)   # move right
#     distance = distance - interval
#     pyautogui.dragRel(0, distance, dur)   # move down
#     pyautogui.dragRel(-distance, 0, dur)  # move left
#     distance = distance - interval
#     pyautogui.dragRel(0, -distance, dur)  # move up


# Scroll the mouse

# Getting a screenshot
# im = pyautogui.scre)enshot()
# print(im.getpixel((50, 200))

# Analyzing the screenshot
# print(pyautogui.pixelMatchesColor(50, 200, (222, 186, 197, 255)))

# Image recognition
# imageLocation = pyautogui.locateOnScreen('flower.png')
# print(imageLocation)
# #
# coordination = pyautogui.center(imageLocation)
# print(coordination)
# #
# pyautogui.click(coordination)
#
# print(list(pyautogui.locateAllOnScreen('flower.png')))

# Sending a string from the keyboard
# pyautogui.click(100, 100)
# pyautogui.typewrite('Hello world!\n')
# pyautogui.typewrite('Hello world!\n', 0.25)
# pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], 0.25)

# Key Names
# print(pyautogui.KEYBOARD_KEYS)
# import pprint
# pprint.pprint(pyautogui.KEYBOARD_KEYS)

# Pressing and Releasing the Keyboard
time.sleep(2)
# pyautogui.keyDown('shift')
# pyautogui.press('2')
# pyautogui.keyUp('shift')

# pyautogui.press('@')

# typewrite(): type a string into a text field
# press(): single-key commands

# Hotkey Combinations
pyautogui.PAUSE = 1
pyautogui.click(100, 100)
pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
pyautogui.hotkey('option', 'right')
pyautogui.hotkey('command', 'v')






