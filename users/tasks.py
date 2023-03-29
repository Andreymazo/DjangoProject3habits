import datetime
import time

import pytz
from celery import shared_task

from config import settings
from config.celery import app
from users.models import Habit, User

# await bot.send_message(chat_id=settings.BOT_CHAT_ID, text="Текст сообщения...")# release Python 3.13???????????
import telepot
from telepot.loop import MessageLoop

BOT_CHAT_ID = settings.MY_CHAT_ID
telegramBot = telepot.Bot(settings.BOT_TOKEN)
# text = 'Time waits for nobody'
bot = telepot.Bot(settings.BOT_TOKEN)
CHAT_ID = settings.CHAT_ID


# @gulnara_domik
# def send_message(text):
#     telegramBot.sendMessage(CHAT_ID, text, parse_mode="Markdown")


@shared_task
def send_telegram():  #(self, request, *args, **kwargs)
    print('_______________________')
    textt = 'Time waits for nobody'
    #while True:
    # if request.method == 'GET':
            #time.sleep(25)  ##Kazhdie 30 sec proveryaet pole time_to_doo_habit
            # thread = threading.Thread(  # создание отдельного потока
            #     target=print, args=("данные сайта обновились",))
            # thread.start()
            # now = time.time()
    now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))
    a = Habit.objects.all()  # time_to_doo_habit.second
    for ii in User.objects.all():
        for i in a.filter(client_id=ii):
            time_compare = (now - i.updated_at).total_seconds() % 86400
            time.sleep(1)
            try:
                # print('(now - i.updated_at).total_seconds()-----', time_compare)##Ostatok secund v sutkah, ego potom sravnit nado
                # print('i.time_to_doo_habit.second_____', i.time_to_doo_habit)
                # i.time_to_doo_habit = datetime.now().time()
                seconds = (
                                  i.time_to_doo_habit.hour * 60 + i.time_to_doo_habit.minute) * 60 + i.time_to_doo_habit.second
                # print(seconds)  ##Vsego secund vo vremeni dlia ispolnenia 86400 sec v sutk, ostatok ot 86400 nas interesuet

                if abs(seconds - time_compare) < 30:  # Esli menshe polminuti do vremeni, otsilaem
                    print('Otsilaem *****************')  ###Zdes mozhno otsilat v telegramm
                print('Ne otsilaem poka *****************')

            except AttributeError as e:
                print(e)
                pass
                # for i in a:
                #     print(dir(i))
                # delta = abs(seconds - now)
        print('now-----77777777777-----', now)
        ######################################################Commentim chtobi ne slalo ######################
        # response=bot.sendMessage(CHAT_ID, textt)#501573655
        # print(response)
        ################################################################################3
        # params = {'chat_id': '-524797982', 'text': 'OKEY!', 'reply_to_message_id': 1508}
        # response = bot.getUpdates()
        # now = datetime.datetime.now(pytz.timezone(settings.TIME_ZONE))


        # return self.queryset(request, *args, **kwargs)
        #self.queryset


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
