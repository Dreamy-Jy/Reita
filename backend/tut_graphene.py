"""
What are the key value arguments for the types.
What are the arguements for the 

Our GraphQL Schema can act as a check for our database.

Resolver must return data in the form of an object that has the same variables as specfied in the type schema. [not check with the offical docs]

Consider mapping the flow of data spec through the db and api.


Use camelCase over snake_case for graphene schema objects...

We'll need to learn to control/understand the SQLAchemy Engine.
"""

import graphene
from tut_sqla import engine, BookModel, Base
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
        session_data = session.query(BookModel).all()
        print("\n`resolve_books` finished\n\n")
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

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

harry_potter = BookModel(title="Harry Potter")
spks_ap = BookModel(title="The Spook's Apprentice", completed=True)
grey = BookModel(title="Fifty Shades of Grey")

session.add(harry_potter)
session.add(spks_ap)
session.add(grey)

session.commit()


print(schema.execute('{ books { title, bookId }}', context={'db_connect': session}).data['books'])
print(schema.execute('mutation { createBook (bookData: {title:"Fifty Shades Darker",completed:true}) { book { title, completed, creationDatetime, bookId } } }', context={'db_connect': session}).data)
