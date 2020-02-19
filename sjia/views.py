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

def results_log(request):
    return render(request, 'results_log.html')

def chart(request):
    return  render(request, 'chart.html')
