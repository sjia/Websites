from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Case
from .serializers import TestcaseSerializers

# Create your views here.
class TestViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    # queryset = Tests.objects.all().order_by('-cid')
    queryset = Case.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = TestcaseSerializers

    @api_view(['GET','POST'])
    def getlist(request,format=None):
        if request.method == 'GET':
            meizis = Case.objects.all()
            serializer = TestcaseSerializers(meizis, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = TestcaseSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)