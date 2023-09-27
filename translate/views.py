from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
import json
client_id = "cGwhwDRITcSEobTG98HL"
secret = "mNrbhhkyEC"


# Create your views here.
@api_view(['POST'])
def translate(request):
    text = request.data['t']
    translate_api = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        'X-Naver-Client-Id' : client_id,
        'X-Naver-Client-Secret' : secret
    }
    data = {
        "source" : "ko",
        "target" : "ja",
        "text" : text
    }
    response = requests.post(translate_api, headers=headers, data=data).json()
    return Response(response)


@api_view(['POST'])
def code(request):
    text = request.data['t']
    code_api = "https://openapi.naver.com/v1/papago/detectLangs"
    headers = {
        'X-Naver-Client-Id' : client_id,
        'X-Naver-Client-Secret' : secret
    }
    data = {
        "query" : text
    }
    response = requests.post(code_api, headers=headers, data = data).json()
    return Response(response)