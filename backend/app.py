# coding=utf-8
""" 
Dreamy Jy back at it again...


"""
from flask import Flask
from flask_graphql import GraphQLView
from api import schema
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
""" The Following are the lessons learned in developing this project

~~~~ Lessons form the App ~~~~
Query Object - why?

Code needs to be writen to handle any possible errors in the database

Lesson: When importing between packages in your project, import "globally" w/o any leading "."s.


~~~~ Lessons from the Schema ~~~~
What are the key value arguments for the types.
What are the arguements for the 

Our GraphQL Schema can act as a check for our database.

Resolver must return data in the form of an object that has the same variables as specfied in the type schema. [not check with the offical docs]

Consider mapping the flow of data spec through the db and api.


Use camelCase over snake_case for graphene schema objects...

We'll need to learn to control/understand the SQLAchemy Engine.


You need your resolvers to raise errors.

"""