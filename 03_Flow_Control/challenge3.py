import pihat_widget as ph
import time

if __name__ == '__main__':

    light = ph.TrafficLight()

    light.set_state("100")  # Red Off Off
    time.sleep(3)
    light.set_state("001")  # Off Off Green
    time.sleep(2)

    light.close()