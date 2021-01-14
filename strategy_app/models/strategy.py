from mongoengine import *


connect("myDatabase")

class Price(Document):
	Option = StringField()
	S = DecimalField(precision=5)
	K = DecimalField(precision=5)
	r = DecimalField(precision=5)
	sigma = DecimalField(precision=5)
	t = DecimalField(precision=5)
	C = DecimalField(precision=5)
	Coupon = DecimalField(precision=5)
	Barrier = DecimalField(precision=5)

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
	prices = ListField(ReferenceField(Price, reverse_delete_rule=PULL))

Strats = Strategy.objects