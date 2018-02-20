from time import sleep
from gpiozero import LED, Buzzer

def dit(x, y, rate):
    led = LED(x)
    buzz = Buzzer(y)
    led.on()
    buzz.on()
    sleep(rate)
    led.off()
    buzz.off()
    sleep(rate)

def dah(x, y, rate):
    led = LED(x)
    buzz = Buzzer(y)
    led.on()
    buzz.on()
    sleep(rate*3)
    led.off()
    buzz.off()
    sleep(rate)

def space(x, y, rate):
    led = LED(x)
    buzz = Buzzer(y)
    led.off()
    buzz.off()
    sleep(rate*3)
