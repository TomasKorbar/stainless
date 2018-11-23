from flask import Flask, Blueprint
from stainless.routes import routes

application = Flask(__name__)
application.register_blueprint(routes)

if __name__ == "__main__":
	application.run("0.0.0.0",5000,True)
