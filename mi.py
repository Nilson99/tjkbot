import random
import time
a = int(input())
if a == 23:
    for i in range(10):
        time.sleep(5)
        print('PUSH')
        if i == 6:
            print('STOP')
            quit()
        
