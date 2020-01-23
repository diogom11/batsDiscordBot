import threading

def timer_run():
    
#Se start for true, é pra iniciar o timer. Se chamar a função e for false é pra parar
def timerToCs(time_t, start): 
    timer = threading.Timer(time_t, timer_run)
    if(start):
        timer = threading.Timer(time_t, timer_run)
        timer.start()
    else:
        timer.stop()
