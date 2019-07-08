# import pyperclip
# pyperclip.copy('浮世繁华')

#
# import clipboard
# clipboard.copy("天龙八部")


# str = '经济'

import subprocess

# subprocess.run(['echo', str, '|pbcopy'])

# p1 = subprocess.Popen(['echo', str], stdout = subprocess.PIPE)
# p2 = subprocess.Popen(['pbcopy'], stdin=p1.stdout, stdout=subprocess.PIPE)

import pyautogui
# from tkinter import Tk
#
# string1 = '古道西风瘦马'
#
# # pyautogui.click((100, 100))
#
# r = Tk()
# r.withdraw()
#
# r.clipboard_clear()
# r.clipboard_append(string1)
# r.update()  # now it stays on the clipboard after the window is closed
#
# r.destroy()


from tkinter import Tk
import time

# schoolList = ['星宿派','神龙教','移花宫','日月神教','逍遥','古墓']
# r = Tk()
# r.withdraw()
# pyautogui.click((100, 100))
# for item in schoolList:
# 	r.clipboard_clear()
# 	r.clipboard_append(item)
# 	r.update() # now it stays on the clipboard after the window is closed
#
# 	print(r.clipboard_get())
#
# 	pyautogui.hotkey('command', 'v')
#
# 	pyautogui.press('\n')
#
# r.destroy()

# 剪切板输出也不正常,莫名其妙freeze

str = '午夜星河'
# print(str.encode('utf-8'))

# at that time, output is messy
p1 = subprocess.Popen(['echo', str], stdout = subprocess.PIPE)
p2 = subprocess.Popen(['pbcopy'], stdin=p1.stdout)

# print(p1.stdout)
# output1 = p1.communicate()[0]
# print(output1)
# # #
# import chardet
# print(chardet.detect(output1))
# print(output1.decode('utf-8'))

'''
https://stackoverflow.com/questions/7165108/in-os-x-lion-lang-is-not-set-to-utf-8-how-to-fix-it

确保terminal敲入locale后，显示的是：
LANG="en_US.UTF-8"  
LC_COLLATE="en_US.UTF-8"  
LC_CTYPE="en_US.UTF-8"  
LC_MESSAGES="en_US.UTF-8"  
LC_MONETARY="en_US.UTF-8"  
LC_NUMERIC="en_US.UTF-8"  
LC_TIME="en_US.UTF-8"  
LC_ALL="en_US.UTF-8"  

否则就要编辑文件
~/.bash_profile 
and append those lines

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

备注：查看隐藏文件 command+shift+.
'''

# read Chinese character from clipboard and manually paste

# p1 = subprocess.Popen(['echo', str], stdout=subprocess.PIPE)
# p2 = subprocess.Popen(['pbcopy'], stdin=p1.stdout, stdout=subprocess.PIPE)

# automate paste with hotkey

# pyautogui.click((100, 100))
# pyautogui.hotkey('command', 'v')


# extend to Chinese character list

# pyautogui.click((100, 100))
# list1 = ['天空', '大地', '山川', '河流']

# empty the clipboard
# subprocess.Popen(['pbcopy'], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE)
#
# for item in list1:
# #
# 	print(list1.index(item), item)
# 	p1 = subprocess.Popen(['echo', item], stdout=subprocess.PIPE)
# 	p2 = subprocess.Popen(['pbcopy'], stdin=p1.stdout, stdout=subprocess.PIPE)
#
# 	pyautogui.press(str(list1.index(item)))
# 	pyautogui.press('\b')
# #
# 	pyautogui.hotkey('command', 'v')
# 	pyautogui.press('\n')






