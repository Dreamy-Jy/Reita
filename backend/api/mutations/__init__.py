import graphene
from .create_book import CreateBook

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()