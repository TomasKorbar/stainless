from stainless.rpi_modules.motor_functions.motor import Motor

motor_left = Motor([19,13,6,5])
motor_right = Motor([21,16,20,26])
arm_lower = Motor([3,17,27,22])
arm_higher = Motor([24,25,1,12])

def move_forward(distance):
	while distance > 0:
		motor_right.turn(10)
		motor_left.turn(10)
		distance -= 1

def turn_left(angle):
	while angle > 0:
		motor_right.turn(10)
		angle -= 1

def turn_right(angle):
	while angle > 0:
		motor_left.turn(10)
		angle -= 1
