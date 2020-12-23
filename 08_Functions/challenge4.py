import pihat_widget as ph
import time

if __name__ == '__main__':

    #            r   g  b
    red_color = 255, 0, 0
    light = ph.LEDMatrix()
    light.set_pixel(0, 1 , red_color)
    time.sleep(5)
    light.close()