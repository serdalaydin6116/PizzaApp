from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Size, Pizza
from .forms import PizzaForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'pizza/home.html')


def pizzas(request):
    pizzas=Pizza.objects.all()
    
    context = {
        "pizzas" : pizzas,
        
    }
    return render(request, "pizza/pizzas.html", context)



def order(request):
    form = PizzaForm()

    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your order created successfully")
            return redirect("list")

    context = {
        "form" : form
    }

    return render(request, "pizza/order.html", context)

def edit_order(request, id):
    pizza = Pizza.objects.get(id=id)
    form = PizzaForm(instance=pizza)

    if request.method == "POST":
        form = PizzaForm(request.POST, instance=pizza)
        if form.is_valid():
            form.save()
            return redirect("list")

    context = {
        "pizza" : pizza,
        "form" : form
    }

    return render(request, "pizza/edit_order.html", context)
