from gpiozero import Servo
from time import sleep

#https://gpiozero.readthedocs.io/en/stable/recipes.html#servo

servo = Servo(14)


servo.min()
sleep(2)
servo.min()
sleep(2)
servo.max()
