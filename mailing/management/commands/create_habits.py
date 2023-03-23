from django.core.management import BaseCommand

from users.models import User, Habit


class Command(BaseCommand):

    # if_pleasant = models.ForeignKey('self', **NULLABLE, on_delete=models.CASCADE, related_name='canbewith_useful',
    #                                 verbose_name='привычка, которую можно привязать к выполнению полезной привычки')
    # if_connected = models.ForeignKey('self', **NULLABLE, on_delete=models.CASCADE, related_name='mustbewith_useful',
    #                                  verbose_name='привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных')
    # period = models.CharField(max_length=100, verbose_name='периодичность выполнения привычки для напоминания в днях')
    # prize = models.CharField(max_length=150, verbose_name='чем пользователь должен себя вознаградить после выполнения')
    # time_fulfil = models.CharField(max_length=100,
    #                                verbose_name='время, которое предположительно потратит пользователь на выполнение привычки')
    # is_published = models.BooleanField(**NULLABLE,
    #                                    verbose_name='привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки')

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

        place = {'walk_outside': 'outside',
                 'feed_pet': 'kitchen',
                 'contrast_shower': 'bath',
                 'russian_bath': 'bath'
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
        for i in User.objects.all():  # .filter(id=Habit.client.id).first()
            for ii in useful_habits:
        # for iii in if_plesant_useful_habits:
        #     # if ii == iii:
        #     #     print('i, iii ------- ',  i, if_plesant_useful_habits[iii])
        #     for iiii in if_connected_useful_habbits:
        #         # if ii==iiii:
        #         #     print('i, iiii============', i, if_connected_useful_habbits[iiii])
                for iiiii in place:
                    # if ii==iiiii:
                    #     print('i, iiiii ________________', i, place[iiiii])
                    for iiiiii in time_fulfil:
                        for iiiiiii in prize:
                            for iiiiiiii in period:
                                habit_list.append(

                                    Habit
                                        (
                                        client=i,
                                        place=place[iiiii],
                                        action=ii,
                                        useful=True,
        # if_pleasant=if_plesant_useful_habits[iii],
        # # {
        #             "client":f'{if_plesant_useful_habits[iii].client}',
        #             "place":f'{if_plesant_useful_habits[iii].place}',
        #             "action":f'{if_plesant_useful_habits[iii].action}',
        #             "useful": True,
        #
        # },
        # if_connected=if_connected_useful_habbits[iiii],
                                      time_fulfil=time_fulfil[iiiiii],
                                      prize=prize[iiiiiii],
                                      period=period[iiiiiiii]
                                            )
                                                )

        Habit.objects.bulk_create(habit_list)
        ##################################################Potom stavim kluchi kak ukazano vishe
        # habit_list = []
        # for ii in User.objects.all():
        #     for i in Habit.objects.all().filter(client_id=ii):
        #         # print(i)
        #         for iii in if_plesant_useful_habits:
        #             # print(iii,i)
        #             if iii == str(i):  ##Pitaus sravnit iteriruemuu privichku klienta s privichkoi sviazannoi s drugoi
        #                 # print("=++++++++++++++++++++++++++++++++++++++++++++++")
        #
        #                 # print(if_plesant_useful_habits[iii])
        #                 g = Habit.objects.all().filter(action=if_plesant_useful_habits[iii])
        #                 for k in g:
        #                     print(k)  # __dict__)
        #                 i.if_pleasant = Habit(
        #                         if_pleasant=Habit.objects.all().filter(action=if_plesant_useful_habits[iii]).first(),
        #                     )
        #                 habit_list.append(
        #                     Habit(
        #                         if_pleasant=if_plesant_useful_habits[iii],
        #                     )
        #                 )
        # Habit.objects.bulk_create(habit_list)

        # habit_list = []
        # for i in User.objects.all():#.filter(id=Habit.client.id).first()
        #     for ii in useful_habits:
        #         for iii in if_plesant_useful_habits:
        #             # if ii == iii:
        #             #     print('i, iii ------- ',  i, if_plesant_useful_habits[iii])
        #             for iiii in if_connected_useful_habbits:
        #                 # if ii==iiii:
        #                 #     print('i, iiii============', i, if_connected_useful_habbits[iiii])
        #                     for iiiii in place:
        #                         # if ii==iiiii:
        #                         #     print('i, iiiii ________________', i, place[iiiii])
        #                             for iiiiii in time_fulfil:
        #                                 for iiiiiii in prize:
        #                                     for iiiiiiii in period:
        #
        #                                         habit_list.append(
        #
        #                                         Habit
        #                                             (
        #                                             client=i,
        #                                             place=place[iiiii],
        #                                             action=ii,
        #                                             useful=True,
        #                                             if_pleasant=if_plesant_useful_habits[iii],
        #                                             # {
        #                                             #             "client":f'{if_plesant_useful_habits[iii].client}',
        #                                             #             "place":f'{if_plesant_useful_habits[iii].place}',
        #                                             #             "action":f'{if_plesant_useful_habits[iii].action}',
        #                                             #             "useful": True,
        #                                             #
        #                                             # },
        #                                             if_connected=if_connected_useful_habbits[iiii],
        #                                             time_fulfil=time_fulfil[iiiiii],
        #                                             prize=prize[iiiiiii],
        #                                             period=period[iiiiiiii]
        #                                         )
        #                                         )
        #
        # Habit.objects.bulk_create(habit_list)
