from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from numpy.core.fromnumeric import product
from .models import Items,Demand
import pandas as pd
from django.views.generic import TemplateView
from .forms import *
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.
@login_required(login_url='login')
def items_list(request):
    ite=None

    try:
        ite=request.user.items.all()
    except ObjectDoesNotExist:
        messages.info(request,"There is no items.")
    form = ItemSearchForm(request.POST or None)

    if request.method == 'POST':
            try:
                ite = request.user.items.filter(name__icontains=form['name'].value())
            except ObjectDoesNotExist:
                messages.info(request,"There is no items.")
    return render(request,'data/items_list.html',context = {"form": form,"items":ite})


@login_required(login_url='login')
def demand_list(request):
    demand=Demand.objects.all()
    return render(request,'data/demand_list.html',context={'demand':demand})



@login_required(login_url='login')
def ItemCreate(request):
        form=ItemsForm()
        if request.method == 'POST':
            form=ItemsForm(request.POST) 
            if form.is_valid():
                n = form.cleaned_data["name"]
                l = form.cleaned_data["lead_time"]
                c = form.cleaned_data["carrying_cost"]
                o = form.cleaned_data["ordering_cost"]
                q = form.cleaned_data["total_inventory"]
                for i in request.user.items.all():
                    if i.name==n:
                        messages.error(request, n +' Item Already Created')
                        return redirect('data:item_create_url')

                t = Items(name=n,lead_time=l,carrying_cost=c,ordering_cost=o,total_inventory=q)
                t.save()
                request.user.items.add(t) 
                messages.success(request, n +' Item Created')
                return redirect('data:items_list_url')
                    
        return render(request,'data/item_create.html',context={'form':form})



@login_required(login_url='login')
def delete_items(request,pk):
    query_set=Items.objects.get(id=pk)
    if request.method=='POST':
        query_set.delete()
        messages.success(request,query_set.name + ' Removed')
        return redirect('data:items_list_url')
    context={'item':query_set.name}
    return render(request,'data/delete_items.html',context)


@login_required(login_url='login')
def update_items(request,pk):
    query_set=Items.objects.get(id=pk)
    form=ItemsForm(instance=query_set)
    n=query_set.name
    if request.method=='POST':
        form=ItemsForm(request.POST,instance=query_set)
        if form.is_valid():
            form.save()
            messages.info(request, n + '  Updated to ' + query_set.name)
            return redirect('data:items_list_url')
    context={'form':form}
    return render(request,'data/update_item.html',context)

"""def view(response):
    return render(response, "data/view.html", {})"""
	
	



def issue_items(request, pk):
    queryset = Items.objects.get(id=pk)
    form=IssueForm()

    if request.method=='POST':
        form=IssueForm(request.POST,instance=queryset)
        if form.is_valid():
            queryset.total_inventory -= queryset.issue_quantity
            form.save()

            return redirect('data:items_list_url')
    context = {"queryset":queryset,"form":form}
    return render(request, "data/add_items.html", context)

def add_inventory(request, pk):
    queryset = Items.objects.get(id=pk)
    form=IssueForm()

    if request.method=='POST':
        form=IssueForm(request.POST,instance=queryset)
        if form.is_valid():
            queryset.total_inventory += queryset.issue_quantity
            form.save()

            return redirect('data:items_list_url')
    context = {"queryset":queryset,"form":form}
    return render(request, "data/add_inventory.html", context)





    










