# coding=utf-8
""" 
Dreamy Jy back at it again...


Query Object - why?

Code needs to be writen to handle any possible errors in the database
"""
from flask import Flask
from flask_graphql import GraphQLView
from tut_graphene import schema
from database import engine, Base, Session

Base.metadata.create_all(engine) # move to setup
session = Session()

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
        get_context=lambda : {'db_connect': session}
    )
)

if __name__ == "__main__":
    app.run(host='0.0.0.0')