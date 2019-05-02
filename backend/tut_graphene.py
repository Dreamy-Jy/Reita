"""
What are the key value arguments for the types.
What are the arguements for the 

Our GraphQL Schema can act as a check for our database.

Resolver must return data in the form of an object that has the same variables as specfied in the type schema. [not check with the offical docs]

Consider mapping the flow of data spec through the db and api.


Use camelCase over snake_case for graphene schema objects...

We'll need to learn to control/understand the SQLAchemy Engine.


You need your resolvers to raise errors.
"""

import graphene
from database import Base, engine
from database.book_model import BookModel
from sqlalchemy.orm import sessionmaker
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class Book(SQLAlchemyObjectType):
    class Meta:
        model = BookModel

class Query(graphene.ObjectType):
    books = graphene.List(Book) # graphene.Field(Book)
    
    def resolve_books(self, info):
        print("\n\n`resolve_books` running\n")
        session = info.context.get('db_connect')
        session_data = session.query(BookModel).all() # NOTE: When SQLAchemcy doesn't know where your db is queries raise errors
        print("\n`resolve_books` finished\n\n")
        # TODO the connection between the format of the data and bookschema type to
        # ... likily to loose to depend on
        return session_data

class BookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    completed = graphene.Boolean(default_value=False)

class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)
    
    book = graphene.Field(Book)

    def mutate(self, info, book_data):
        print("\n\n`create_book` running\n")
        session = info.context.get('db_connect')

        book = BookModel(title=book_data.title, completed=book_data.completed)

        session.add(book)
        session.commit()
        print("\n`create_book` finished\n\n")
        return CreateBook(book=book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)