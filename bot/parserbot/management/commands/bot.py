from django.core.management.base import BaseCommand
from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.utils.request import Request
from django.conf import settings
from parserbot.models import Profile


def create_db(update: Update, context: CallbackContext):
    user = update.message.from_user.first_name + ' ' + update.message.from_user.last_name
    external_id = update.message.from_user.id



    text = update.message.text
    hw_1, hw_2, hw_3 = '#марафон_дз_1', '#марафон_дз_2', '#марафон_дз_3'
    if text.find(hw_1) != -1:
        Profile.objects.get_or_create(
            external_id=external_id,
            defaults={
                'name': user,
                'score_homework_1': 1,
                'score_homework_2': 0,
                'score_homework_3': 0,
                'total_score': 0,
            }
        )
    elif text.find(hw_2) != -1:
        Profile.objects.get_or_create(
            external_id=external_id,
            defaults={
                'name': user,
                'score_homework_1': 1,
                'score_homework_2': 1,
                'score_homework_3': 0,
                'total_score': 0,
            }
        )
    elif text.find(hw_3) != -1:
        Profile.objects.get_or_create(
            external_id=external_id,
            defaults={
                'name': user,
                'score_homework_1': 1,
                'score_homework_2': 1,
                'score_homework_3': 1,
                'total_score': 0,
            }
        )


class Command(BaseCommand):
    help = 'run bot'

    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=getattr(settings, 'PROXY_URL', None),
        )
        updater = Updater(
            bot=bot,
            use_context=True,
        )

        print(bot.get_me())

        message_handler = MessageHandler(Filters.text, create_db)
        updater.dispatcher.add_handler(message_handler)

        updater.start_polling()
        updater.idle()
