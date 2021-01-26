from gpiozero import AngularServo
from time import sleep

#https://gpiozero.readthedocs.io/en/stable/recipes.html#servo

servo = AngularServo(17, min_angle=0, max_angle=180)
servo.angle = 0

print('zero...')
sleep(3)

while True:
    servo.angle = 180
    sleep(2)
    #servo.angle = 90
    #sleep(2)
    servo.angle = 0
    sleep(2)
