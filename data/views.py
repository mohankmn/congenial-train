from django.shortcuts import get_object_or_404, render
from numpy.core.fromnumeric import product
from .models import Items,Demand
import pandas as pd
from django.views.generic import TemplateView
from .forms import *
from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import reverse


# Create your views here.

def items_list(request):
    items=Items.objects.all()
    return render(request,'data/items_list.html',context={'items':items})

def demand_list(request):
    demand=Demand.objects.all()
    return render(request,'data/demand_list.html',context={'demand':demand})

def ItemCreate(request):
        form=ItemsForm()
        if request.method == 'POST':
            form=ItemsForm(request.POST) 
            if form.is_valid():
                form.save()
                return redirect('data:items_list_url')
                    
        return render(request,'data/item_create.html',context={'form':form})

class DemandCreate(View):
    def get(self,request):
        form=DemandForm()
        return render(request,'data/demand_create.html',context={'form':form})

    def post(self,request):
        bound_form = DemandForm(request.POST)
        if bound_form.is_valid():
            new_demand=bound_form.save()
            form=DemandForm()
            return render(request,'data/demand_create.html',context={'form':form})

        
def delete_items(request,pk):
    query_set=Items.objects.get(id=pk)
    if request.method=='POST':
        query_set.delete()
        return redirect('data:items_list_url')
    return render(request,'data/delete_items.html')

def update_items(request,pk):
    query_set=Items.objects.get(id=pk)
    form=ItemsForm(instance=query_set)
    if request.method=='POST':
        form=ItemsForm(request.POST,instance=query_set)
        if form.is_valid():
            form.save()
            return redirect('data:items_list_url')
    context={'form':form}
    return render(request,'data/item_create.html',context)







