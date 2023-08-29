from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)

    
button.when_pressed = led.toggle

    
    

pause()