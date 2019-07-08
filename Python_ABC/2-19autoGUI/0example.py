# for demostration for autoGUI

import pyautogui, time, csv

# Dragging the mouse
# https://www.sumopaint.com/paint/

# time.sleep(3)
# pyautogui.click()    # click to put drawing program in focus
# distance = 200
# interval = 5
#
# D = 0.1
#
# # Dragging the Mouse
#
# while distance > 0:
#     pyautogui.dragRel(distance, 0, duration=D)   # move right
#     distance = distance - interval
#     pyautogui.dragRel(0, distance, duration=D)   # move down
#     pyautogui.dragRel(-distance, 0, duration=D)  # move left
#     distance = distance - interval
#     pyautogui.dragRel(0, -distance, duration=D)  # move up


# from tkinter import Tk
#
# customers = []
#
# partyFile = open('party.csv', encoding='utf-8')
# partyReader = csv.reader(partyFile)
#
# for row in partyReader:
# 	if partyReader.line_num == 1:
# 		continue
#
# 	food = row[3]
# 	foods = food.split()
# 	customer = {
# 		'school': row[0],
# 		'attend': row[1],
# 		'headcount': row[2],
# 		'foodOption': foods,
# 		'taboos': row[4],
# 		'contact': row[5]
# 	}
# 	customers.append(customer)
# partyFile.close()
#
# pyautogui.click((100, 100))
#
# for customer in customers:
#
# 	r = Tk()
# 	r.withdraw()
# 	r.clipboard_clear()
# 	r.clipboard_append(customer['taboos'])
# 	r.update()  # now it stays on the clipboard after the window is closed
#
# 	pyautogui.hotkey('command', 'v')
# 	pyautogui.press('\n')
#
# 	r.destroy()

import subprocess
customers = []

partyFile = open('party.csv', encoding='utf-8')
partyReader = csv.reader(partyFile)

for row in partyReader:
	if partyReader.line_num == 1:
		continue

	food = row[3]
	foods = food.split()
	customer = {
		'school': row[0],
		'attend': row[1],
		'headcount': row[2],
		'foodOption': foods,
		'taboos': row[4],
		'contact': row[5]
	}
	customers.append(customer)
partyFile.close()

pyautogui.click((100, 100))

# add: empty clipboard, doesn't work
# subprocess.Popen(['pbcopy'], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE)
#
# for customer in customers:
#
# 	p1 = subprocess.Popen(['echo', customer['taboos']], stdout=subprocess.PIPE)
# 	p2 = subprocess.Popen(['pbcopy'], stdin=p1.stdout, stdout=subprocess.PIPE)
#
# 	pyautogui.hotkey('command', 'v')

# add index, work
for customer in customers:

	p1 = subprocess.Popen(['echo', customer['taboos']], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(['pbcopy'], stdin=p1.stdout, stdout=subprocess.PIPE)
	pyautogui.press(str(customers.index(customer)))
	pyautogui.press('\b')
	pyautogui.hotkey('command', 'v')

