from rest_framework import serializers
from models import Employee
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import exceptions

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        #fields = ('first_name','last_name')
        fields = "__all__"



# LoginView Serializer is a class which validates if the user is login or not
class LoginViewSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get("username","")
        password = data.get("password","")

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is inactive"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Invalid username or password"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Please provide username and password."
            raise exceptions.ValidationError(msg)
        
        return data