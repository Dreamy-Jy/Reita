import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.models import BookModel

'''
TODO rename this class
TODO give this class a name
'''
class Book(SQLAlchemyObjectType):
    class Meta:
        model = BookModel
        description = "A type represent a book. Is connected to our databases representation of books."