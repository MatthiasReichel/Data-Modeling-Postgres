import graphene
from graphene_django import DjangoObjectType
from .models import Users, Songplays

class UserType(DjangoObjectType):
    class Meta:
        model = Users

class SongplayType(DjangoObjectType):
    class Meta:
        model = Songplays
     
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    songplays = graphene.List(SongplayType)

    def resolve_songplays(self, info, **kwargs):
        return Songplays.objects.all()

    def resolve_users(self, info, **kwargs):
        return Users.objects.all()
        #.select_related('user_id')
        #test1 = Songplays.objects.all()
    
    #def resolve_users(self, info, **kwargs):
    #    return Users.objects.select_related('user_id').all()