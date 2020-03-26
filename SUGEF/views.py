from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *

hora = timezone.now().hour

def login(request):
      return render(request, 'login.html', {})
