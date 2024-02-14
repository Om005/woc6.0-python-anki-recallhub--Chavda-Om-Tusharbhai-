
import time
timestamp = time.strftime('%H:%M:%S')
a = int(time.strftime('%H'))
if __name__=="__main__":
    if(a>0 and a<11):
        print("Good morning, sir.")
    elif(a>=11 and a<18):
        print("Good afternoon, sir.")
    else:
        print("Good evening, sir.")