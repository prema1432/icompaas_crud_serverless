from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)

from app.routes.user_routes import UserResource

api.add_resource(UserResource, "/users", "/users/<int:user_id>")


@app.route("/")
def home():
    return jsonify(message="Welcome to the homepage!")


with app.app_context():
    db.create_all()
