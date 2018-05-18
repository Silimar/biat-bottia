from bottia import settings
from response_bottia import greetings, goodbye, askjoke, reclamation


class Core_Response:

    def determine(intente):
        if intente == "greetings":
            greetings.Greetings.greetings()
        if intente == "goodbye":
            goodbye.Goodbye.goodbye()
        if intente == "ask-joke":
            askjoke.AskJoke.askjoke()
        if intente == "reclamation":
            reclamation.Reclamation.reclamation()