from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from . import Base

class BookModel(Base):
    __tablename__ = 'books'
    bookId = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(Boolean, default=False)
    creationDateTime = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<Book(id=\'%s\', title=\'%s\', completed=\'%s\', creationDatetime=\'%s\')>' % (self.book_id, self.title, self.completed, self.creationDatetime)
