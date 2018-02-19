#Import packages/functions
print("Loading...")
from gpiozero import LED, Buzzer
import time
print("Done")

#set variables
rate = 0.15
led = LED(int(input("Which pin is the LED connected to?: ")))
buzz = Buzzer(int(input("Which pin is the Buzzer connected to?: ")))

#led patterns
def dit():
    led.on()
    buzz.on()
    time.sleep(rate)
    led.off()
    buzz.off()
    time.sleep(rate)

def dah():
    led.on()
    buzz.on()
    time.sleep(rate*3)
    led.off()
    buzz.off()
    time.sleep(rate)

def space():
    led.off()
    buzz.off()
    time.sleep(rate*6)

def alarm(x):
    for i in range(x):
        dit()
        dit()
        dit()
        time.sleep(rate)
        dah()
        dah()
        dah()
        time.sleep(rate)
        dit()
        dit()
        dit()
        space()

#Set up the alarm
print("Time: "+str(time.localtime()[3])+":"+str(time.localtime()[4]))
alarmtime = input("Set an alarm for? (hr:min): ")
print("Alarm set for "+alarmtime+".")


#checks to see if the alarm should go off
while True:
    timehr = str(time.localtime()[3])
    timemin = str(time.localtime()[4])
    if alarmtime == timehr+":"+timemin:
        print("It's "+alarmtime+"!")
        alarm(13)
    

