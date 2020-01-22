import threading

def timer_run():
    print("has ran\n")

def timetest(time_t, start): 
    
    timer = threading.Timer(time_t, timetest)
    timer.start()
    print("Exit\n")

    
    #timer.cancel()