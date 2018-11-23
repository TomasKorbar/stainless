from flask import Flask, Blueprint, Request, request

routes = Blueprint('routes', __name__)

@routes.route('/move/forward', methods=["GET"])
def move_forward():
	return str(request.args.get('cm'))

@routes.route('/move/turn')
def turn():
	return '1'

@routes.route('/trash/isinrange')
def isinrange():
	return '1'

@routes.route('/trash/pickup')
def pickup():
	return '1'
