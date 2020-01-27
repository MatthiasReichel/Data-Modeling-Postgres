from rest_framework import serializers
from .models import Users, Songplays

class UsersSerializer(serializers.ModelSerializer):
	first_name = serializers.Field(source='Users.first_name')
	last_name = serializers.Field(source='Users.last_name')
	gender = serializers.Field(source='Users.gender')
	level = serializers.Field(source='Users.level')

	class Meta:
		model = Users
		fields = ('songplay_id', 'user_id', 'first_name', 'last_name', 'gender', 'level')