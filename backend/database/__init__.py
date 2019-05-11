# coding=utf-8
'''
Dreamy Jy back at it agian...


'''

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


inorder to use a session between modules you need a link to persisting database

__next:__
1. Learn to add constraints to columns.
2. Delete items from db
3. Pass Database access
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from constants import db_url

engine = create_engine(db_url)
Base = declarative_base()
Session = sessionmaker(bind=engine)
