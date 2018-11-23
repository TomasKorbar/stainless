import stainless.rpi_modules.motor_functions.robot_controll as rbcontroll
from flask import Flask, Blueprint, Request, request
import subprocess

routes = Blueprint('routes', __name__)

@routes.route('/move/forward', methods=["GET"])
def move_forward():
	_execute_alone(1, int(request.args.get("cm")))
	return "1"

@routes.route('/move/turn', methods=["GET"])
def turn():
	if int(request.args.get("angle")) > 0:
		_execute_alone(4,int(request.args.get("angle")))
	else:
		_execute_alone(3,-1 * int(request.args.get("angle")))
	return "1"

@routes.route('/trash/isinrange')
def isinrange():
	return '1'

@routes.route('/trash/pickup')
def pickup():
	return '1'

def _execute_alone(action, val):
	subprocess.call([
		'python3',
		'/usr/lib/python3.5/stainless/rpi_modules/motor_functions/robot_controll',
		str(action),
		str(val)
		])
