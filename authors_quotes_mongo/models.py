from mongoengine import Document
from mongoengine.fields import DateTimeField, ListField, StringField, ReferenceField

class Authors(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()

class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Authors)
    quote = StringField()