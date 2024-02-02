from flask import request
from flask_restful import Resource

from app import db
from app.models.user_models import IcompasUser
from app.schemas.user_schema import IcompasUserSchema

user_schema = IcompasUserSchema()
users_schema = IcompasUserSchema(many=True)


class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = db.session.get(IcompasUser, user_id)
            if not user:
                return {'message': 'User not found'}, 404
            serialized_users = user_schema.dump(user)
            return serialized_users

        else:
            users = IcompasUser.query.all()
            serialized_users = users_schema.dump(users)
            return serialized_users

    def post(self):
        try:
            data = request.get_json()
            errors = user_schema.validate(data)
            if errors:
                return {"message": "Validation errors", "errors": errors}, 400
            new_user = IcompasUser(**data)
            db.session.add(new_user)
            db.session.commit()
            serialized_user = user_schema.dump(new_user)
            return serialized_user, 201

        except Exception as e:
            return {"message": "An error occurred", "error": str(e)}, 500

    def put(self, user_id):
        try:
            user = db.session.get(IcompasUser, user_id)
            if not user:
                return {'message': 'User not found'}, 404
            data = request.get_json()
            errors = user_schema.validate(data, partial=True)
            if errors:
                return {"message": "Validation errors", "errors": errors}, 400
            user.email = data.get('email', user.email)
            user.first_name = data.get('first_name', user.first_name)
            user.last_name = data.get('last_name', user.last_name)
            user.password = data.get('password', user.password)
            db.session.commit()
            serialized_user = user_schema.dump(user)
            return serialized_user, 200
        except Exception as e:
            return {"message": "An error occurred", "error": str(e)}, 500

    def delete(self, user_id):
        try:
            user = db.session.get(IcompasUser, user_id)
            if not user:
                return {'message': 'User not found'}, 404
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}, 204
        except Exception as e:
            return {"message": "An error occurred", "error": str(e)}, 500
