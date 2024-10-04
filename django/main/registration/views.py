from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .utils import generate_code_verifier
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def VerifyRoblox(request):
    redirect_uri = "http://localhost:8000/accounts/roblox/redirect"
    state = "STATE_HERE"
    code_challenge = generate_code_verifier()
    finalUrl = f'https://apis.roblox.com/oauth/v1/authorize?client_id=5136978817459521000&code_challenge={code_challenge}&code_challenge_method=S256&redirect_uri={redirect_uri}&scope=openid%20profile&response_type=code&state={state}'
    return redirect(finalUrl)
#https://www.django-rest-framework.org/topics/html-and-forms/