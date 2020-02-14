from django.urls import path, include
import sjia.views

urlpatterns = [
    path('index', sjia.views.index),
    path('resultlog', sjia.views.resultlog),
    path('chart', sjia.views.chart)
]