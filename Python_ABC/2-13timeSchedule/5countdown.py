# # countdown.py - A simple countdown script.
#
import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft = timeLeft - 1

#
print('Music, Now!')
subprocess.run(['open', '像风一样自由.mp3'])

