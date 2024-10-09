from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from .utils import generate_code_verifier, generate_code_challenge, check_roblox_token
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import get_user_model
from .models import RobloxUser

UserBase = get_user_model()

#from django.middleware.csrf import get_token
# Create your views here.


@api_view(['GET'])
@ensure_csrf_cookie
def VerifyRoblox(request):
    redirect_uri = "http://localhost:8000/accounts/roblox/redirect"
    state = get_token(request)
    request.session['state'] = state
    code_verifier = generate_code_verifier()
    code_challenge = generate_code_challenge(code_verifier)

    request.session['code_verifier'] = code_verifier
    
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

    if state != request.session['state']:
        return JsonResponse({"error": "State does not match. Possible CSRF attack!"}, status=403)
    if not code:
        return JsonResponse({"error": "No code provided"}, status=400)
    
    token_url = 'https://apis.roblox.com/oauth/v1/token'

    payload = {
        'client_id': settings.ROBLOX_CLIENT_ID,
        'client_secret': settings.ROBLOX_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'code_verifier': request.session['code_verifier']
    }

    response = requests.post(token_url, data=payload)

    if response.status_code == 200:
        token_data = response.json()
        TokenValid = check_roblox_token(token_data.get('access_token'))
        if TokenValid != False:

            newUser = RobloxUser.objects.create(
                robloxID = TokenValid.get('userID'),
            )

            newUser.save()

            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        print("Error:", response.status_code, response.json())
        return HttpResponse(status=400)
    


class StaffRegistration(APIView):
    def get(self, request):
        
        return render(request, 'bot/registration/staff.html', {})