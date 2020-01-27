from django.db import models
from rest_framework import serializers

class Songplays(models.Model):
	songplay_id = models.TextField(primary_key=True)
	start_time = models.BigIntegerField(blank=True)
	user_id = models.ForeignKey('Users', on_delete=models.CASCADE, db_column='user_id')
	song_id = models.TextField(blank=False)
	artist_id = models.TextField(blank=True)
	session_id = models.TextField(blank=True)

	class Meta:
		db_table = 'songplays'

class Users(models.Model):
	user_id = models.TextField(primary_key=True)
	first_name = models.CharField(max_length=30, blank=True) 
	last_name = models.CharField(max_length=30, blank=True)
	gender = models.CharField(max_length=1, blank=True)
	level = models.CharField(max_length=4, blank=True)

	class Meta:
		db_table = 'users'

class SongplaysSerializer(serializers.ModelSerializer):
	first_name = serializers.ReadOnlyField(source='user_id.first_name')
	#last_name = serializers.Field(source='Users.user_id.last_name')
	#gender = serializers.Field(source='Users.user_id.gender')
	#level = serializers.Field(source='Users.user_id.level')
	#users = UserSerializer(many=True, read_only=True)

	#users = serializers.SerializerMethodField()

	class Meta:
		model = Songplays
		fields = ['songplay_id', 'first_name']

	#def get_users(self, obj):
	#	qs = obj.exercises.all()
	#	return UserSerializer(qs, many=True, read_only=True).data