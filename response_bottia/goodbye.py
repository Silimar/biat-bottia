from random import randint

from bottia.models import Response


class Goodbye:

    def goodbye(self):
        ress = Response.objects.filter(Intents_id=2)
        x = randint(0, len(ress))
        res = ress[x].text
        return res