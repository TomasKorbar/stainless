from flask import Flask, Blueprint, Request, request
import subprocess

routes = Blueprint('routes', __name__)

@routes.route('/move/forward', methods=["GET"])
def move_forward():
	return str(_execute_alone(1, int(request.args.get("cm"))))

@routes.route('/move/turn', methods=["GET"])
def turn():
	if int(float(request.args.get("angle"))) > 0:
		_execute_alone(4,int(float(request.args.get("angle"))))
	else:
		_execute_alone(3,-1 * int(float(request.args.get("angle"))))
	return "1"

@routes.route('/trash/pickup')
def pickup():
	return '1'

def _execute_alone(action, val):
	ec = subprocess.call([
		'python3',
		'/usr/lib/python3.5/stainless/rpi_modules/motor_functions/robot_controll.py',
		str(action),
		str(val)
		])
	return ec
