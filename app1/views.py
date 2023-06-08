from django.shortcuts import render

# Create your views here.
from app1.models import *
from rest_framework.decorators import api_view
from app1.serializers import *
from rest_framework.response import Response
from rest_framework import status

@api_view()
def Employeejdata(request):
    EQS=Employee.objects.all() #list of employee objects
    ESD=EmployeeMS(EQS,many=True)# json variable is ESD
    return Response(ESD.data,status=status.HTTP_201_CREATED)
