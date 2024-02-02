from flask_marshmallow.sqla import SQLAlchemyAutoSchema

from app.models.user_models import IcompasUser


class IcompasUserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = IcompasUser
