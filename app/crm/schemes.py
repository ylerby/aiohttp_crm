from marshmallow import Schema, fields

from app.web.schemes import OkResponseSchema


class UserAddSchema(Schema):
    email = fields.Str(required=True)


class UserSchema(UserAddSchema):
    id = fields.UUID(required=True)


class UserGetRequestSchema(Schema):
    id = fields.UUID(required=True)


class UserGetSchema(Schema):
    user = fields.Nested(UserSchema)


class UserGetResponseSchema(OkResponseSchema):
    data = fields.Nested(UserGetSchema)


#Здесь получаем объект, который будет сериализован схемой UserSchema
class ListUserSchema(Schema):
    users = fields.Nested(UserSchema, many=True)


#Мы получаем массив со всеми пользователями, переопределяем data из OkResponseSchema
class ListUsersResponseSchema(OkResponseSchema):
    data = fields.Nested(ListUserSchema)
