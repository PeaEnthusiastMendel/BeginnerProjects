#Import modules
print("Loading...")
from gpiozero import LED, Buzzer
from time import sleep
print("Ready")

#set variables
rate = float(int(input("Enter the speed of transmission (recommended is 15): "))/100)
led = LED(int(input("Which pin is the LED connected to?: ")))
buzz = Buzzer(int(input("Which pin is the Buzzer connected to?: ")))

# Dictionary representing the morse code chart
morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#Translate into Morse Code
def translate(text):
    cipher = ''
    for letter in text:
        if letter != ' ':
            # translates one letter and adds a space
            cipher += morse_dict[letter] + ' '
        else:
            cipher += ' '
 
    return cipher

def message():
    text = str(input("Enter English here: "))
    result = translate(text.upper())
    return result


#translates morse code into led patterns
def dit():
    led.on()
    buzz.on()
    sleep(rate)
    led.off()
    buzz.off()
    sleep(rate)

def dah():
    led.on()
    buzz.on()
    sleep(rate*3)
    led.off()
    buzz.off()
    sleep(rate)

def space():
    led.off()
    buzz.off()
    sleep(rate*3)
        

#display morse code through led
while True:
    code = message()
    print(code)
    for i in range(len(code)):
        if (code[i]== '-'):
            dah()
        elif (code[i]== '.'):
            dit()
        elif (code[i]== ' '):
            space()

            
        

