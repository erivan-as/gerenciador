# -*- encoding: utf-8 -*-
"""
#from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse(u"Olá mundo!")
"""
from django.shortcuts import render, redirect,get_object_or_404
from models import ItemAgenda
from forms import FormItemAgenda
def adiciona_(request):
    if request.method == 'POST': # Formulário enviado
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        # Exibe formulário em branco
        form = FormItemAgenda()
    return render(request, "adiciona.html", {'form': form})
def adiciona(request):
    form = FormItemAgenda(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "adiciona.html", {'form': form})
    
def remove(request, nr_item):
    item = get_object_or_404(ItemAgenda, pk=nr_item)
    if request.method=="POST":
        item.delete()
        return redirect("/")
    return render(request, "remove.html", {'item': item})

def item(request, nr_item):
    item = get_object_or_404(ItemAgenda, pk=nr_item)
    form = FormItemAgenda(request.POST or None,
                          request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "item.html", {'form': form})

def index(request):
     lista_itens = ItemAgenda.objects.all()
     return render(request, "lista.html",
                   {'lista_itens': lista_itens})
