import time
from threading import Thread


def countdown(n):
    if t.is_alive():
        print("Still running")
    while n > 0:
        print(n)
        n -= 1
        time.sleep(3)

t = Thread(target=countdown, args=(10,))

t.start()
