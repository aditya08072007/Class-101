import time
seconds = input("Enter the time in the number of seconds")
def countdown_timer(seconds):
    while seconds > 0:
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer,end = '\r')
        time.sleep(1)
        seconds-=1
    print('time up')
countdown_timer(int(seconds))
