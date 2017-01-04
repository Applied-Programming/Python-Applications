import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer: " + name + " Started\n")
    tLock.acquire()
    print(name+" Has acquired has the lock\n")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat = -1
    print(name + " is releasing the lock\n")
    tLock.release()
    print("Timer: " + name + " Completed\n")


def Main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main Completed\n")


if __name__ == '__main__':
    Main()
