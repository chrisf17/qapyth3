# PROBLEM: Create an OO Traffic Light System
# 1. Write code for a UK Traffic light
# 2. Write code for a US Traffic Light
# 3. Advanced: Improve your design as far as you can in the time.

import pihat_widget as ph
import time

red = 0xFF, 0, 0
green = 0, 0xFF, 0
amber = 0xFF, 0xBF, 0
off = 0, 0,  0

def main():
    board = ph.LEDMatrix()
    board.set_pixel(0, 0, red)
    board.set_pixel(0, 1, amber)
    board.set_pixel(0, 2, green)

    time.sleep(5)

    board.close()

if __name__ == '__main__':

    main()