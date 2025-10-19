from django.shortcuts import render
# Create your views here.

def index(request):
  blogs = [
    {'title': "Learning Django",'content': "Django is an awesome open source framework for building APIs using Django REST framework.", 'author': "Buony Tut", 'date': "2025.06.04"},
    {'title': "Learning Django",'content': "Django is an awesome open source framework for building APIs using Django REST framework.", 'author': "Buony Tut", 'date': "2025.06.04"},
    {'title': "Learning Django",'content': "Django is an awesome open source framework for building APIs using Django REST framework.", 'author': "Buony Tut", 'date': "2025.06.04"},
    {'title': "Learning Django",'content': "Django is an awesome open source framework for building APIs using Django REST framework.", 'author': "Buony Tut", 'date': "2025.06.04"},
  ]

  context = {'blogs': blogs}
  return render (request, 'index.html', context)


def about(request):

  return render(request, 'about.html')

def contact(request):

  return render(request, 'contact.html')