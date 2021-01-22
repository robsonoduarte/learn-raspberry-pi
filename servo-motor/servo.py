from gpiozero import Servo
from time import sleep

#https://gpiozero.readthedocs.io/en/stable/recipes.html#servo

servo = Servo(17)
servo.value = 0

while True:
    servo.value = -1
    sleep(2)
    servo.value = 0
    sleep(2)
    servo.value = 1
    sleep(2)
