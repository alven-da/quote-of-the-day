from mongoengine import Document, StringField

class QuoteDocument(Document):
    meta = {'collection': 'quotes'}
    author = StringField(required=True)
    quote = StringField(required=True)