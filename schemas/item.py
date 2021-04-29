from ma import ma
from models.item import ItemModel
from models.store import StoreModel

class ItemSchema(ma.ModelSchema):
    class Meta:
        model = ItemModel # will look into the UserModel class for the needed fields and create it 
        load_only = ('store',) # store field for loading schema only and not in dump. Comma after the field makes it a tuple
        dump_only = ('id',) # opposite o load_only. An ID is not needed from the user when creating a new record. It will be done by the model
        include_fk = True