from django.shortcuts import render, HttpResponse
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


@csrf_exempt
def sms_response(request):

    param = request.data('param', None)
    print(param)

    return HttpResponse(param)

    # if request.method == 'POST':
    #
    #     resp = MessagingResponse()
    #     msg = resp.message("Check out this sweet owl!")
    #
    #     return HttpResponse(str(resp))
    # else:
    #     return HttpResponse('teste')