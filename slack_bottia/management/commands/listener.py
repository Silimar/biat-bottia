from django.core.management.base import BaseCommand

from bottia import core_bottia
from slack_bottia.models import Team
from slackclient import SlackClient
import time


class Command(BaseCommand):
    help = 'Starts the bot for the first'

    def handle(self, *args, **options):
        team = Team.objects.first()
        client = SlackClient(team.bot_access_token)
        if client.rtm_connect():
            while True:
                events = client.rtm_read()
                print("%s----%s" % (team, events))
                for event in events:
                    if 'type' in event and event['type'] == 'message':
                        response = core_bottia.Core_Bottia.core_bottia_func(event['text'])
                        client.rtm_send_message(event['channel'], response)
                time.sleep(1)
