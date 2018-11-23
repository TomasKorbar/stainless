import time
import gpiod

from stainless.rpi_modules import consts

class Motor():
	def __init__(self, pins):
		self._chip = gpiod.Chip("gpiochip0")
		self._lines = self._chip.get_lines(pins)
		self._lines.request(consumer="gpiochip0",
			type=gpiod.LINE_REQ_DIR_OUT
		)
		self._current_step = 0

	def turn(self, angle):
		target_angle = angle
		next_step = 1 if target_angle > 0 else 0
		while target_angle > consts.HALFSTEP_ANGLE or target_angle < -consts.HALFSTEP_ANGLE:
			self._lines.set_values(consts.HALFSTEP_SEQUENCE[self._current_step])
			self._current_step += next_step
			if self._current_step > 7:
				self._current_step = 0
			else if self._current_step < 0:
				self._current_step = 7
			time.sleep(0.001)

if __name__ == "__main__":
	m = Motor([2,3,4,17])
	m.turn(90)
