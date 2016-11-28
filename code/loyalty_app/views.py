from django.shortcuts import render
from django.utils import timezone
from . import models
from models import Users

def post_list(request):
    posts = Users.objects.all()
    return render(request, 'post_list.html', {'posts': posts})