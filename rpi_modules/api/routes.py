from flask import Flask, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/move/forward')
def move_forward():
	pass

@routes.route('/move/turn')
def turn():
	pass

@routes.route('/trash/isinrange')
def isinrange():
	pass

@routes.route('/trash/pickup')
def pickup():
	pass
