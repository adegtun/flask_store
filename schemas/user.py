from marshmallow import Schema, fields

class UserSchema(Schema):
    class Meta:
        load_only = ('password',) # user password field for loading schema only and not in dump. Comma after the field makes it a tuple
        dump_only = ('id',) # opposite o load_only. An ID is not needed from the user when creating a new record. It will be done by the model
    id = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)