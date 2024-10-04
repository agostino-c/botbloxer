from django.urls import path
from . import views

urlpatterns = [
    path('roblox/verify/', views.VerifyRoblox),
]
