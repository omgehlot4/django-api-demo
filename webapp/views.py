# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token
from models import Employee
from serializer import EmployeeSerializer, LoginViewSerializer

from django.shortcuts import render

# Create your views here.

class EmployeeView(APIView):
    authentication_classes = (TokenAuthentication,)
    def get(self,request):
        all_employees = Employee.objects.all()
        print(all_employees)
        serilalizer = EmployeeSerializer(all_employees, many= True)
        return Response(serilalizer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class LoginView(APIView):
    '''
        LoginView class is an APIView which handles
        the token management
    '''
    def post(self,request):
        serializer = LoginViewSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key}, status= 200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication)
    def post(self, request):
        django_logout(request)
        return Response(status=204)