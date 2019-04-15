# coding=utf-8
'''

What is the engine?
What is the declarative base?

How do we pass in database access?


Does using different declaritive base change the engine's ability to create for us?

How do we create an the following with the use of special
helper functions?
 - Engine
 - Session

We Use sessions to make queries.
Queries are made with Query objects, why?

__next:__
1. Learn to add constraints to columns.
2. Delete items from db
3. Pass Database access


'''

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class BookModel(Base):
    __tablename__ = 'books'

    bookId = Column(Integer, primary_key=True)
    title = Column(String)
    completed = Column(Boolean, default=False)
    creationDatetime = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return "<Book(id='%s', title='%s', completed='%s', creationDatetime='%s')>" % (self.book_id, self.title, self.completed, self.creationDatetime)