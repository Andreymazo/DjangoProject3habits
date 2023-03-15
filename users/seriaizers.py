from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from users.models import Habit


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

class HabitSerializer(serializers.ModelSerializer):

#     # has_subscrpt_curr_user = serializers.SerializerMethodField()

    class Meta:
        model = Habit
        fields = '__all__'

#["client", "place", "time_todo", "is_published", "period"]
