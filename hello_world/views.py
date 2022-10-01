from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def hello_json(request):
    return JsonResponse({"Name": "Hello World!"})