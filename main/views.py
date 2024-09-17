from django.shortcuts import render, redirect
from main.forms import ItemForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    items = Item.objects.all()

    context = {
        'nama_aplikasi' : 'Pandas Pet Store',
        'nama' : 'Muhammad Rafli Esa Pradana',
        'class' : 'PBP-D',
        'items' : items,
    }

    return render(request, "main.html", context)


def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST" :
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_item.html", context)


def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")