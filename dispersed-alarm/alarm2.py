#Import packages/functions
print("Loading...")
from gpiozero import LED, Buzzer
import time
import text2morse as t2m
print("Done")

#set variables
rate = 0.15
led = int(input("Which pin is the LED connected to?: "))
buzz = int(input("Which pin is the Buzzer connected to?: "))

#led patterns
def alarm():
    for i in range(3):
        t2m.dit(led, buzz, rate)
        t2m.dit(led, buzz, rate)
        t2m.dit(led, buzz, rate)
        time.sleep(rate)
        t2m.dah(led, buzz, rate)
        t2m.dah(led, buzz, rate)
        t2m.dah(led, buzz, rate)
        time.sleep(rate)
        t2m.dit(led, buzz, rate)
        t2m.dit(led, buzz, rate)
        t2m.dit(led, buzz, rate)
        t2m.space(led, buzz, rate)

#Set up the alarm
print("Time: "+str(time.localtime()[3])+":"+str(time.localtime()[4]))
alarmtime = input("Set an alarm for? (hr:min): ")
print("Alarm set for "+alarmtime+".")


#checks to see if the alarm should go off
#repeats until the minute is over
while True:
    timehr = str(time.localtime()[3])
    timemin = str(time.localtime()[4])
    if alarmtime == timehr+":"+timemin:
        print("It's "+alarmtime+"!")
        alarm()
    

