# pybricksdev run ble challenge1.py
# library imports
from techbrick import *

# variables
left = Motor(Port.B)
right = Motor(Port.A)
left_a = Motor(Port.F)
right_a = Motor(Port.E)

# main
if __name__ == "__main__":
    gyro_straight(3.5, 20, left, right)
    gyro_left(30, left, right)