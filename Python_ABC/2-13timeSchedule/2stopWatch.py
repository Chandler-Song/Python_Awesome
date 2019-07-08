# stopwatch.py - A simple stopwatch program.

import time

# Display instruction
print('Press Enter to begin. Afterwards, press ENTER to "click" the stopwatch. '
      'Press Ctrl-C(Windows) Command-F2(Mac) to quit.')

input() # press Enter to begin
print('Started.')
startTime = time.time() # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #{}: {} ({})'.format(lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Command-F2 or Ctrl-C exception to keep its error message from displaying
    print('\nDone.')
