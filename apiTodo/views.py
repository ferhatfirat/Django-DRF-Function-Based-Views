from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>')


@api_view(['GET'])
def todoList(request):
    querset = Todo.objects.all()
    serializer = TodoSerializer(querset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todoListCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET", 'POST'])
def toDo_list(request):
    
    if request.method == "GET":
        querset = Todo.objects.all()
        serializer = TodoSerializer(querset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["PUT"])
def todoListUpdate(request, pk):
    querset = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=querset, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def todoListDeelete(request, pk):
    querset = Todo.objects.get(id=pk)
    querset.delete()
    return Response("item deleted")

@api_view(["GET", 'PUT', "DELETE"])
def todoListDetail(request, pk):
    
    if request.method == "GET":
        querset = Todo.objects.get(id=pk)
        serializer = TodoSerializer(querset)
        return Response(serializer.data)
    elif request.method == "PUT":
        querset = Todo.objects.get(id=pk)
        serializer = TodoSerializer(instance=querset, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        querset = Todo.objects.get(id=pk)
        querset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)