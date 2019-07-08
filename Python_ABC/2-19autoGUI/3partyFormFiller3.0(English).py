# partyFormFiller.py - Automatically fills in the form (English character).
# 运行前要切换到英文输入

import pyautogui, time, csv

# Set these to the correct coordinates for your particular computer.3
schoolField = (439, 486)
submitButton = (474, 544)
submitButtonColor = (49, 123, 253)
submitAnotherLink = (478, 422)

# custermer list from csv file
customers = []

# convert to dictionary variable
partyFile = open('partyEnglish.csv', encoding='utf-8')
partyReader = csv.reader(partyFile)

# read data from csv file
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

# slow down pace of pyautogui action
pyautogui.PAUSE = 1

# get form window on focus
pyautogui.click((100, 100))

# full screen
pyautogui.hotkey('ctrl', 'command', 'f')


# automate filling in form
for customer in customers:

    # To confirm the form is ready to fill in

    # To bottom of the page
    pyautogui.hotkey('command', 'down')
    # Wait until the form page has loaded.
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)

    # To top of the page for input
    pyautogui.hotkey('command', 'up')

    schoolList = ['少林', '武当', '昆仑', '峨眉', '五岳', '逍遥', '丐帮', '全真', '古墓', '移花宫']
    school = int(customer['school'])
    print('Entering {} info...'.format(schoolList[school-1]))

    # Click the first field
    pyautogui.click(schoolField[0], schoolField[1])

    # Fill out the 门派 field.
    for order in range(school):
        pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('\t')

    # Fill out the 是否参加 field.
    if customer['attend'] == '1':
        pyautogui.typewrite(['space', '\t'])
    elif customer['attend'] == '2':
        pyautogui.typewrite(['down', 'space', '\t'])
    elif customer['attend'] == '3':
        pyautogui.typewrite(['down', 'down', 'space', '\t'])

    # # Fill out 多少人 field.
    pyautogui.typewrite(customer['headcount'] + '\t', 0.25)

    # Fill out 食物 field.
    # 1-肉夹馍；2-山东大饼；3-手撕饼；4-煎饼果子 5-馒头；6-肉包子；7-素馅包子

    if '1' in customer['foodOption']:
        pyautogui.typewrite(['space', '\t'])
    else:
        pyautogui.press('\t')

    if '2' in customer['foodOption']:
        pyautogui.typewrite(['space', '\t'])
    else:
        pyautogui.press('\t')

    if '3' in customer['foodOption']:
        pyautogui.typewrite(['space', '\t'])
    else:
        pyautogui.press('\t')

    if '4' in customer['foodOption']:
        pyautogui.typewrite(['space', '\t'])
    else:
        pyautogui.press('\t')

    if '5' in customer['foodOption']:
        pyautogui.typewrite(['space', '\t'])
    else:
        pyautogui.press('\t')

    if '6' in customer['foodOption']:
        pyautogui.typewrite(['space', '\t'])
    else:
        pyautogui.press('\t')

    if '7' in customer['foodOption']:
        pyautogui.typewrite(['space', '\t'])
    else:
        pyautogui.press('\t')

    # Fill out 禁忌 field.
    pyautogui.typewrite(customer['taboos']+'\t', 0.25)

    # Fill out 手机号码 field.
    pyautogui.typewrite(customer['contact']+'\t', 0.25)

    # Click Submit.
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')

    # Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])