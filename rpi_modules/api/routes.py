from flask import Flask, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/move/forward')
def move_forward():
	return '1'

@routes.route('/move/turn')
def turn():
	return '1'

@routes.route('/trash/isinrange')
def isinrange():
	return '1'

@routes.route('/trash/pickup')
def pickup():
	return '1'
