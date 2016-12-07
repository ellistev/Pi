import RPi.GPIO as GPIO
import time

def ToggleLights(on):
    print('toggle lights')
    #GPIO.cleanup()
    if on:
        tailpin = 29
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(tailpin, GPIO.OUT)
        GPIO.output(lightpin, GPIO.HIGH)
        GPIO.output(tailpin, True)
        print('blink on')
    else:
        tailpin = 29
        GPIO.output(tailpin, False)
        GPIO.cleanup()
        print('blink off')
    
    return

def EnableLights():
    print('enable lights')
    GPIO.cleanup()
    tailpin = 29
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(tailpin, GPIO.OUT)
    GPIO.cleanup()
    return

