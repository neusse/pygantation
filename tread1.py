from threading import Thread
from time import sleep

cnt = 0
def threaded_function(arg, frase, _tm):
    global cnt
    for i in range(arg):
        print(cnt, frase)
        sleep(_tm)
        cnt += 1


if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (5,  "uno", .3))
    thread2 = Thread(target = threaded_function, args = (7, "[due]", .5))
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()
    print("thread finished...exiting")