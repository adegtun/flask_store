from ma import ma
from models.user import UserModel

class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel # will look into the UserModel class for the needed fields and create it 
        load_only = ('password',) # user password field for loading schema only and not in dump. Comma after the field makes it a tuple
        dump_only = ('id',) # opposite o load_only. An ID is not needed from the user when creating a new record. It will be done by the model
        # Removing the duplication since flask Marshmallow will handle it