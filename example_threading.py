import threading

def keepalive():
    print('Alive.')
    threading.Timer(2, keepalive).start()
    print(threading.active_count())

threading.Timer(20, keepalive).start()