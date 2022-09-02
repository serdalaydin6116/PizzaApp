from django.shortcuts import render
from django.http import HttpResponse
from .models import Size, Pizza

# Create your views here.
def home(request):
    # todos = Todo.objects.all()
    # form = TodoForm()
    # context = {
    #     "todos" : todos,
    #     "form" : form
    # }

    return render(request, "pizza/home.html")
