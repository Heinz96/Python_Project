from mongoengine import *


connect("myDatabase")

class Comment(Document):
	content = StringField()

class Author(EmbeddedDocument):
	name = StringField()

class Strategy(Document):
	author = EmbeddedDocumentField(Author)
	name = StringField(required=True)
	image = StringField(required=False)
	description = StringField(required=False)
	comments = ListField(ReferenceField(Comment, reverse_delete_rule=PULL))

Strats = Strategy.objects