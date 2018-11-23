import stainless.rpi_modules.motor_functions.robot_controll as rbcontroll
from flask import Flask, Blueprint, Request, request

routes = Blueprint('routes', __name__)

@routes.route('/move/forward', methods=["GET"])
def move_forward():
	rbcontroll.move_forward(int(request.args.get("cm")))
	return str("1")

@routes.route('/move/turn', methods=["GET"])
def turn():
	if int(request.args.get("angle")) > 0:
		rbcontroll.turn_right(int(request.args.get("angle")))
	else:
		rbcontroll.turn_left(-1 * int(request.args.get("angle")))
	return "1"

@routes.route('/trash/isinrange')
def isinrange():
	return '1'

@routes.route('/trash/pickup')
def pickup():
	return '1'
