from django.core.management import BaseCommand

from users.models import User, Habit


class Command(BaseCommand):

    def handle(self, *args, **options):
        # emails = ['test@testtest.ru', 'foreig_papa@papa.com']
        useful_habits = ['laugh', 'read_something', 'walk_outside', 'excite_sports', 'walk_pet', 'feed_pet',
                         'hug_somebody', 'do_python', 'contrast_shower', 'russian_bath']
        if_plesant_useful_habits = {'excite_sports': "walk_pet",
                                    'hug_somebody': "laugh"}
        # for i in Habit.objects.all().get(useful_habits[4]).first():
        #     print(**i)
        if_connected_useful_habbits = {'read_something': 'do_python',
                                       'walk_pet': 'walk_outside',
                                       }
##Dopisivaya zdes slovari pri sapuske budut menyatsya polya, naprimer mozno opredelit mesto privichki, kotoroe ese ne opredeleno
        placee = {'walk_outside': 'outside',
                 'feed_pet': 'kitchen',
                 'contrast_shower': 'bath',
                 'russian_bath': 'bath',
                  'excite_sports': 'outside'
                 }
        time_fulfil = {'laugh': 15,
                       'read_something': 30,
                       'walk_outside': 50,
                       'excite_sports': 45,
                       'walk_pet': 30,
                       'feed_pet': 25,
                       'hug_somebody': 15,
                       'do_python': 300,
                       'contrast_shower': 20,
                       'russian_bath': 60
                       }
        prize = {'laugh': '1 choclate',
                 'read_something': '2 choclate',
                 'walk_outside': '3 choclate',
                 'excite_sports': '4 choclate',
                 'walk_pet': '5 choclate',
                 'feed_pet': '6 choclate',
                 'hug_somebody': '7 choclate',
                 'do_python': '8 choclate',
                 'contrast_shower': '9 choclate',
                 'russian_bath': '10 choclate'}
        period = time_fulfil = {'laugh': 1,
                                'read_something': 1,
                                'walk_outside': 1,
                                'excite_sports': 2,
                                'walk_pet': 1,
                                'feed_pet': 1,
                                'hug_somebody': 1,
                                'do_python': 1,
                                'contrast_shower': 1,
                                'russian_bath': 3}
        habit_list = []
        ####################Snachala prosto zapolnyaem privicki bez kluchey self############
        # for i in User.objects.all():  # .filter(id=Habit.client.id).first()
        #     for ii in useful_habits:
        #         # for iiiii in place:
        #             # for iiiiii in time_fulfil:
        #                 # for iiiiiii in prize:
        #                     # for iiiiiiii in period:
        #                         habit_list.append(
        #                             Habit
        #                                 (
        #                                 client=i,
        #                                 # place=place[iiiii],
        #                                 action=ii,
        #                                 useful=True,
        #                                 # time_fulfil=time_fulfil[iiiiii],
        #                                 # prize=prize[iiiiiii],
        #                                 # period=period[iiiiiiii]
        #                                 )
        #                                           )
        #
        # Habit.objects.bulk_create(habit_list)
        ###########################################
        # for i in Habit.objects.all().filter(client_id=id).first():
        # for i in User.objects.all().filter(id=Habit.client.id).first():
        d = Habit.objects.all()
        for i in User.objects.all():
            # print(i.id)users_habit
            d.filter(client_id=i.id)#users_habit
            for j in d:
                # print(j)# 30

                for iiiii in placee:
                    if iiiii == str(j):
                        j.place = placee[iiiii]
                        j.save()

                        # print(iiiii) # 12
                        # print(j.place) #None
                        # print(placee[iiiii])
                # print(j.action)
                #         print(type(j.place))# =
                #         print(type(placee[iiiii]))##Vstavlyaem place

                ####################Snachala prosto zapolnyaem privicki bez kluchey self############
                # for i in User.objects.all():  # .filter(id=Habit.client.id).first()
                #     for ii in useful_habits:
                #         # for iiiii in place:
                #             # for iiiiii in time_fulfil:
                #                 # for iiiiiii in prize:
                #                     # for iiiiiiii in period:
                #                         habit_list.append(
                #                             Habit
                #                                 (
                #                                 client=i,
                #                                 # place=place[iiiii],
                #                                 action=ii,
                #                                 useful=True,
                #                                 # time_fulfil=time_fulfil[iiiiii],
                #                                 # prize=prize[iiiiiii],
                #                                 # period=period[iiiiiiii]
                #                                 )
                #                                           )
                #
                # Habit.objects.bulk_create(habit_list)
                ###########################################