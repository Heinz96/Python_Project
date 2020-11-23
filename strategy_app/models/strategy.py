from mongoengine import *


connect("myDatabase")

class Comment(EmbeddedDocument):
	content = StringField()

class Author(EmbeddedDocument):
	name = StringField()

class Strategy(Document):
	author = EmbeddedDocumentField(Author)
	name = StringField(required=True)
	image = StringField(required=False)
	description = StringField(required=False)
	comments = ListField(EmbeddedDocumentField(Comment))

Strats = Strategy.objects