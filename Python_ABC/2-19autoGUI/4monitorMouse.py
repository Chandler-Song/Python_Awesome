# Get current coordination and color of the mouse cursor
#
from pynput import mouse
import pyautogui

# def on_click(x, y, button, pressed):
#
#     # if button == mouse.Button.right:
#     #     return False
#     #
#     if x<50 and y<50:
#         return False
#
#     if pressed:
#         coordinate = (int(x), int(y))
#         pixelColor = pyautogui.screenshot().getpixel(coordinate)
#         print(coordinate, pixelColor)
#
# # Collect events until released
# with mouse.Listener(
#         on_click=on_click,
# ) as listener:
#         listener.join()


# ctrl+c(windows) or command+f2(Mac) to quit
# def on_click(x, y, button, pressed):
#
#     if pressed:
#         coordination = (int(x), int(y))
#         pixelColor = pyautogui.screenshot().getpixel(coordination)
#         print(coordination, pixelColor)
#
# print('Press fn+command+F2(Mac) or Ctrl+C(windows) to quit.')
# try:
#     # Collect events
#     with mouse.Listener(on_click=on_click) as listener:
#         listener.join()
#
# except KeyboardInterrupt:
#         listener.stop()






# Class

# from pynput import mouse
# import pyautogui
#
#
# class MyException(Exception):
#     pass
#
#
# def on_click(x, y, button, pressed):
#
#     if button == mouse.Button.right:
#         raise MyException(button)
#     # if x<10 and y<10:
#     #     raise MyException(button)
#
#     if pressed:
#         x, y = pyautogui.position()
#         pixelColor = pyautogui.screenshot().getpixel((x, y))
#         print((x, y), pixelColor)
#
# # Collect events until released
# with mouse.Listener(
#         on_click=on_click,
# ) as listener:
#     try:
#         listener.join()
#
#     except MyException:
#         listener.stop()