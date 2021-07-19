from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Option, Menu, Order
from .forms import MenuCreate, OptionCreate, OrderCreate
from django.contrib.auth.decorators import login_required
import arrow
import datetime


def home(request):
    return render(request, 'menuapp/home.html')


@login_required
def menu_create(request):
    if request.method == "POST":
        form = MenuCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuCreate()

    return render(request, 'menuapp/menu_create.html', {'form': form})


@login_required
def menu_list(request):
    menus = Menu.objects.order_by("-menu_date")
    return render(request, 'menuapp/menu_list.html', {'menus': menus})


def menu_detail(request, pk):
    try:
        menu = Menu.objects.get(pk=pk)
        options = Option.objects.filter(menu=menu)
    except Menu.DoesNotExist:
        raise Http404('Menu does not exist')

    return render(request, 'menuapp/menu_detail.html', context={'menu': menu, 'options': options})


@login_required
def menu_delete(request, pk):
    menus = Menu.objects.get(id=pk)
    menus.delete()
    return redirect('menu_list')


@login_required
def option_create(request, pk):
    if request.method == "POST":
        form = OptionCreate(request.POST)
        if form.is_valid():
            form.instance.menu = Menu.objects.get(pk=pk)
            form.save()
        return redirect('menu_detail', pk=pk)
    else:
        form = OptionCreate()
    return render(request, 'menuapp/option_add.html', {'form': form})


@login_required
def option_edit(request, menu_pk, pk):
    if request.method == "POST":
        form = OptionCreate(request.POST, instance=Option.objects.get(pk=pk))
        if form.is_valid():
            form.instance.menu = Menu.objects.get(pk=menu_pk)
            form.save()
        return redirect('menu_detail', pk=menu_pk)
    else:
        form = OptionCreate(instance=Option.objects.get(pk=pk))
    return render(request, 'menuapp/option_add.html', {'form': form})


@login_required
def option_delete(request, menu_pk, pk):
    options = Option.objects.get(id=pk)
    options.delete()
    return redirect('menu_detail', pk=menu_pk)


@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'menuapp/order_list.html', {'orders': orders})


# def order_create(request, menu_pk):
#     if request.method == "POST":
#         form = OrderCreate(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = OrderCreate()
#         form.fields['option_selected'].queryset = Option.objects.filter(menu=menu_pk)
#     return render(request, 'menuapp/order_create.html', {'form': form})

def order_create(request, menu_pk):
    if request.method == "POST":
        form = OrderCreate(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("(っ˘ڡ˘ς) Order received!")
    else:
        now = arrow.get(datetime.datetime.now()).to('America/Santiago')
        time_up = arrow.utcnow().to('America/Santiago').replace(hour=11, minute=0, second=0)
        if now <= time_up:
            form = OrderCreate()
            form.fields['option_selected'].queryset = Option.objects.filter(menu=menu_pk)
        else:
            return HttpResponse("(╯°□°）╯︵ ┻━┻ Time up! You can order until 11")
    return render(request, 'menuapp/order_create.html', {'form': form})
