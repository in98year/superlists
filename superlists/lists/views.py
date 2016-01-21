from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from lists.models import Item


# Create your views here.

def homePage(request):
    return render(request, 'lists/home.html')


def viewList(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', {'items':items})


def newList(request):
    Item.objects.create(text=request.POST.get('itemText'))
    return redirect(reverse('lists:viewList'))