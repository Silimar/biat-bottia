from fbmq import Page, QuickReply

from bottia import settings


class Reclamation:
    def reclamation():
        page = Page
        quick_replies = [
            QuickReply(title="Action", payload="PICK_ACTION"),
            QuickReply(title="Comedy", payload="PICK_COMEDY")
        ]

        page.send(settings.RECIPIENT_ID,
                  'Je te love'
                  #quick_replies=quick_replies
                  )
        return 0