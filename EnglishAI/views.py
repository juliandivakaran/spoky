from django.shortcuts import render
from importlib import import_module
from django.http import HttpResponse
from django.views import View
from django.http import JsonResponse


# Create your views here.
#class indexView(View):
 #   def hello_world(request):
  #      return JsonResponse({'message': 'Hello, World!'})


class indexView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Hello, World! mc'})
