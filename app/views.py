from functools import partial
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudentSerializer
from .models import Student

from rest_framework import status
# Create your views here.
def index(request):
    return render(request, 'index.html')

# @api_view(['GET','POST','PUT','DELETE'])
# def student_api(request):
#     if request.method == 'GET':
#         id = request.data.get('id')
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu.data, many=True)
#         return Response(serializer)


#     if request.method == 'POST':
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Respone':'Data Created'})
#         return Response(serializer.errors)
        

#     if request.method == 'PUT':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         serializer = StudentSerializer(stu,data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'Response':'Data Updated'})
#         return Response(serializer.errors)


#     if request.method == 'DELETE':
#         id = request.data.get('id')
#         stu = Student.objects.get(pk=id)
#         if stu is not None:
#             stu.delete()
#             return Response({'Response':'Deleted'})
#         return Response(serializer.errors)


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Respone':'Complete Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


    if request.method == 'PATCH':
        serializer = StudentSerializer(data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Respone':'Partial Data Created'})
        return Response(serializer.errors)
        

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Response':'Data Updated'})
        return Response(serializer.errors)


    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        if stu is not None:
            stu.delete()
            return Response({'Response':'Deleted'})
        return Response(serializer.errors)


