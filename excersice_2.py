#creating GOOD MORNING  WITH TIME STAMP
import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

name=input("enter your name")
hour=int(time.strftime('%H'))

if(0<=hour<=11):
    print("hello",name,"Good Morning!")
elif(12<=hour<=16):
    print("hello",name,"Good afternoon!")
else:
    print("hello",name,"Good eveneing!")
    

