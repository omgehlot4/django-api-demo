# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Employee
from serializer import EmployeeSerializer 

from django.shortcuts import render

# Create your views here.

class EmployeeView(APIView):
    def get(self,response):
        all_employees = Employee.objects.all()
        print(all_employees)
        serilalizer = EmployeeSerializer(all_employees, many= True)
        return Response(serilalizer.data)

