from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)

while True:
    button.when_pressed = led.on
    #sleep(2)
    button.when_pressed = led.off
    #sleep(2)
    
    

#pause()