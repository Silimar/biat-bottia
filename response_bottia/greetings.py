from random import randint

from bottia.models import Response


class Greetings:

    def greetings(self):
        ress = Response.objects.filter(Intents_id=1)
        x = randint(0, len(ress))
        res = ress[x].text
        return res
