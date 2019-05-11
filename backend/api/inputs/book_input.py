import graphene

class BookInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    completed = graphene.Boolean(default_value=False)