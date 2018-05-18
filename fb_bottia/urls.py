from django.conf.urls import url
from django.urls import path
from fb_bottia.views import BottiaView

urlpatterns = [
    path('b01e1faeeee39b3357125078a66e9c54a3391eee4d50bce30e960/', BottiaView.as_view())
]
