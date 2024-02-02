import awsgi
from flask import Flask
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

with app.app_context():
    db.create_all()


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})
