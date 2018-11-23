from stainless.rpi_modules.motor_functions.motor import Motor
from threading import Thread
import sys

motor_left = Motor([19,13,6,5])
motor_right = Motor([21,16,20,26])
arm_higher = Motor([3,17,27,22])
arm_lower = Motor([24,25,1,12])

def move_forward(distance):
	while distance > 0:
		t1 = Thread(target=lambda: motor_right.turn(100))
		t2 = Thread(target=lambda: motor_left.turn(100))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		distance -= 1

def move_backward(distance):
	while distance > 0:
		t1 = Thread(target=lambda: motor_right.turn(-100))
		t2 = Thread(target=lambda: motor_left.turn(-100))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		distance -= 1

def turn_left(angle):
	while angle > 0:
		t1 = Thread(target=lambda: motor_right.turn(10))
		t2 = Thread(target=lambda: motor_left.turn(-10))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		angle -= 1

def turn_right(angle):
	while angle > 0:
		t1 = Thread(target=lambda: motor_right.turn(-10))
		t2 = Thread(target=lambda: motor_left.turn(10))
		t1.start()
		t2.start()
		t1.join()
		t2.join()
		angle -= 1

def higher_high_arm(angle):
	arm_higher.turn(angle)

def lower_high_arm(angle):
	arm_higher.turn(angle)

def higher_low_arm(angle):
	arm_lower.turn(angle)

def lower_low_arm(angle):
	arm_lower.turn(angle)

if __name__ == "__main__":
	if int(sys.argv[1]) == 1:
		move_forward(int(sys.argv[2]))
	elif int(sys.argv[1]) == 2:
		move_backward(int(sys.argv[2]))
	elif int(sys.argv[1]) == 3:
		turn_left(int(sys.argv[2]))
	elif int(sys.argv[1]) == 4:
		turn_right(int(sys.argv[2]))

