from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.
def register_view(request):
    return HttpResponse('<p>register page</p>')  
def login_view(request):
    pass
def dashboard_vieww(request):
    pass
def logout_view(request):
    pass