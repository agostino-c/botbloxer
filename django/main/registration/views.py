from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import JsonResponse
from .utils import generate_code_verifier
from rest_framework.decorators import api_view
from django.conf import settings
# Create your views here.


@api_view(['GET'])
def VerifyRoblox(request):
    redirect_uri = "http://localhost:8000/accounts/roblox/redirect"
    state = "STATE_HERE"
    code_challenge = generate_code_verifier()
    
    final_url = (
        f'https://apis.roblox.com/oauth/v1/authorize'
        f'?client_id={settings.ROBLOX_CLIENT_ID}'
        f'&code_challenge={code_challenge}'
        f'&code_challenge_method=S256'
        f'&redirect_uri={redirect_uri}'
        f'&scope=openid%20profile'
        f'&response_type=code'
        f'&state={state}'
    )

    return redirect(final_url)



#https://www.django-rest-framework.org/topics/html-and-forms/


@api_view(['GET'])
def VerifyRobloxCallback(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    
    if not code:
        return JsonResponse({"error": "No code provided"}, status=400)
    
    print(code)
    print(state)

    return JsonResponse({"msg": "hellloooo"}, status=200)