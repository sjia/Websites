from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
######################## Form #####################
from django import forms
from django.forms import widgets
from django.forms import fields
from sjia import models
from django.forms import ModelChoiceField

def index(request):
    return render(request,'index.html')

def resultlog(request):
    return render(request, 'requestlog.html')

def chart(request):
    return  render(request, 'chart.html')