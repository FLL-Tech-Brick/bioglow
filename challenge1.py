# pybricksdev run ble challenge1.py
# library imports
from techbrick import *

# variables
left = Motor(Port.A)
right = Motor(Port.F)
# left_a = Motor(Port.F)
# right_a = Motor(Port.E)

# main
if __name__ == "__main__":
    gyro_straight(5, 50, left, right)
    gyro_straight(-5, 50, left, right)
    #gyro_left(30, left, right)