import graphene
from database.models import BookModel
from ..objects import Book
from ..inputs import BookInput

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