from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from notification_sender.views import sms_response

urlpatterns = [
    url(r'^receive/$', sms_response),

]