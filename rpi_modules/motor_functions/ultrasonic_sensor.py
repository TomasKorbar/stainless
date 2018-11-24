import gpiod
import time

class UltrasonicSensor():
    def __init__(self, control_pins):
        self._pins = control_pins

    def distance(self):
        self._chip = gpiod.Chip("gpiochip0")
        # TRIG
        self._trig_line = self._chip.get_line(self._pins[0])
        self._echo_line = self._chip.get_line(self._pins[1])
        self._trig_line.request(consumer="gpiochip0",
            type=gpiod.LINE_REQ_DIR_OUT
        )
        self._echo_line.request(consumer="gpiochip0",
            type=gpiod.LINE_REQ_DIR_IN
        )

        self._trig_line.set_value(1)
        time.sleep(0.00001)
        self._trig_line.set_value(0)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while self._echo_line.get_value() == 0:
            StartTime = time.time()

        # save time of arrival
        while self._echo_line.get_value() == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance_traveled = (TimeElapsed * 34300) / 2
        self._chip.close()
        return distance_traveled
