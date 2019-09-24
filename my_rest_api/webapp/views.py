from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import EmployeesSerializers

class EmployeeList(APIView):

    def get(self,request):
        emp_object = Employees.objects.all()
        serializers = EmployeesSerializers(emp_object, many=True)
        return Response(serializers.data)

    def post(self):
        pass



