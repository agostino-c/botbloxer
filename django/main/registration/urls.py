from django.urls import path
from . import views

urlpatterns = [
    path('roblox/verify/', views.VerifyRoblox),
    path('roblox/redirect', views.VerifyRobloxCallback),

    path('staff/registration', views.StaffRegistration.as_view()),
]
