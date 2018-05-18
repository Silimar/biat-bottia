from random import randint

from bottia.models import Response


class AskJoke:

    def askjoke(self):
        ress = Response.objects.filter(Intents_id=3)
        x = randint(0, len(ress))
        res = ress[x].text
        return res
