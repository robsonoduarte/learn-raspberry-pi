from gpiozero import Servo
from time import sleep

#https://gpiozero.readthedocs.io/en/stable/recipes.html#servo

servo = Servo(17)

while True:
    servo.min()
    sleep(2)
    servo.mid()
    sleep(2)
    servo.max()
    sleep(2)
