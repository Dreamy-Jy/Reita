import graphene
from .book_type import Book
from database.models import BookModel

class Query(graphene.ObjectType):
    books = graphene.List(Book)

    def resolve_books(self, info):
        print("\n\n`resolve_books` running\n")
        session = info.context.get('db_connect')
        session_data = session.query(BookModel).all()
        print("\n`resolve_books` finished\n\n")
          
        return session_data
