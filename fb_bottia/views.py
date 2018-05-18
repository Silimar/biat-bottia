import json
import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from fbmq import Page

import bottia
from bottia import core_bottia
from bottia import settings


class BottiaView(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '4206942069':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid Token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        page = Page(settings.FACEBOOK_ACCESS_TOKEN)

        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print(incoming_message)
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    res = bottia.core_bottia.Core_Bottia.core_bottia_func(message['message']['text'])
                    settings.RECIPIENT_ID = message['sender']['id']
                    print(message)
                    page.send(message['sender']['id'], res)


        return HttpResponse()
