import time
import threading


run = 1


def display():
    global run
    while 1:
        if run == 1:
            print ("hello from outside")
            time.sleep(10)

#import bg_run
t = threading.Thread(target=display)
t.daemon = True
t.start()