from __future__ import print_function
import recastai

client = recastai.Client('d4f4a9f934aec06379fa8b2986d73e0f', 'en')


def rec_call(text):
    response = client.request.analyse_text(text)
    return response.intent.slug
