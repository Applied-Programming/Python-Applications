import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out,"a")
        f.write(self.text)
        f.close()
        time.sleep(2)
        print("Finished Background File Write to " + self.text + "\n")

def Main():
    message = input("Enter a string to store: \n")
    background = AsyncWrite(message,'out.txt')
    background.start()
    print("The program can continue while it writes in another thread \n")
    print("100 + 400 = ", 100+400)

    background.join() #wait till background thread is done
    print("")
    print("Wait till background thread is complete\n")

if __name__ == '__main__':
    Main()

