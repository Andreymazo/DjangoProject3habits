from django.db import models
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from users.models import Habit
NULLABLE = {'blank': True, 'null': True}

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

class HabitSerializer(serializers.ModelSerializer):
    if_pleasant = models.ForeignKey('users.Habit', **NULLABLE, on_delete=models.CASCADE,
                                    related_name='canbewith_useful',
                                    verbose_name='привычка, которую можно привязать к выполнению полезной привычки')
    prize = models.CharField(max_length=150, verbose_name='чем пользователь должен себя вознаградить после выполнения',
                             **NULLABLE)

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('client',)  ##Tolko svoi mozno sozdavat

    def __str__(self):
        return f'{self.prize} {self.if_pleasant}'

    def validate(self, data):  ##Pri sozdanii v adminke ne rabotaet
        """
        Check that start is before finish.
        """

        # if data['start'] > data['finish']:
        #     raise serializers.ValidationError("finish must occur after start")
        # return data
        if data['if_pleasant'] and data['prize']:
            raise serializers.ValidationError('AYAYAYAY')
        return data
#######################################
    # def validate(self, data):##Pri sozdanii v adminke ne rabotaet
    #     """
    #     Check that start is before finish.
    #     """
    #
    #     # if data['start'] > data['finish']:
    #     #     raise serializers.ValidationError("finish must occur after start")
    #     # return data
    #     if data['if_pleasant'] and data['prize']:
    #         raise serializers.ValidationError('AYAYAYAY')
    #     return data
#####################################
# if_pleasant = models.ForeignKey('users.Habit', **NULLABLE, on_delete=models.CASCADE, related_name='canbewith_useful',
#                                 verbose_name='привычка, которую можно привязать к выполнению полезной привычки')
#  prize = models.CharField(max_length=150, verbose_name='чем пользователь должен себя вознаградить после выполнения', **NULLABLE)


# def create(self, validated_data):


#["client", "place", "time_todo", "is_published", "period"]
