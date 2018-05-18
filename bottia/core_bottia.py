from random import randint

from bottia.models import Response, Intents
from recast_bottia import rec_bot
from response_bottia import core_response


class Core_Bottia:

    def core_bottia_func(text):

        #Reconaissance d'Intente
        intent = rec_bot.rec_call(text)

        #Generation de la réponse
        core_response.Core_Response.determine(intent)