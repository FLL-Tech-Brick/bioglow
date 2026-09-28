# THE MAIN FUNCTIONS AND VALUES BANKS FOR IMPORTING
# pybricksdev run ble my_program.py
# imports
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# globals
hub = PrimeHub()

# functions

# main forward function
def gyro_straight(rotations, speed, motor1, motor2):

    # set relative position to 0
    motor1.reset_angle(0)
    motor2.reset_angle(0)


    direction = 1 if rotations >= 0 else -1
    target_degrees = abs(rotations) * 360
    base_speed = speed * 10 * direction

    # reset yaw angle to 0
    hub.imu.reset_heading(0)

    # repeat until B relative position > rotations * 360
    while abs(motor2.angle()) <= target_degrees:
        correction = hub.imu.heading() * -3
        motor1.run(base_speed + correction)
        motor2.run(-(base_speed - correction))
        wait(10)

    # stop moving, then wait 0.5 seconds
    motor1.stop()
    motor2.stop()
    wait(10)

# gyro turn function
def gyro_left(degrees, motor1, motor2):
    
    # set yaw angle to 0
    hub.imu.reset_heading(0)
    
    # repeat
    while abs(hub.imu.heading()) <= abs(degrees) - 2:
        motor1.run(200)
        motor2.run(200)
        wait(5)
    
    # stop moving
    motor1.stop()
    motor2.stop()
    wait(100)

def gyro_right(degrees, motor1, motor2):
    
    # set yaw angle to 0
    hub.imu.reset_heading(0)
    
    # repeat
    while abs(hub.imu.heading()) <= abs(degrees) - 2:
        motor1.run(-200)
        motor2.run(-200)
        wait(5)
    
    # stop moving
    motor1.stop()
    motor2.stop()
    wait(100)

# simpler version for testing
def forward_basic(t, motor1, motor2):
    motor1.run(500)
    motor2.run(-500)
    wait(t)
    motor1.stop()    
    motor2.stop()

def backward_basic(t, motor1, motor2):
    motor1.run(-500)
    motor2.run(500)
    wait(t)
    motor1.stop()    
    motor2.stop()

def left_attachment(t, motor1, direction):
    motor1.run(500*direction)
    wait(t)
    motor1.stop()
