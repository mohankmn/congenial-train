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
    form = ItemSearchForm(request.POST or None)

    if request.method == 'POST':
	        items = Items.objects.filter(name__icontains=form['name'].value())
	        
    return render(request,'data/items_list.html',context = {"form": form,"items":items})

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



"""def issue_items(request, pk):
	queryset = Demand.objects.get(id=pk)
	form = IssueForm(request.POST or None, instance=queryset)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.quantity -= instance.issue_quantity
		instance.save()

		return redirect('data:items_list_url')
		# return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"queryset": queryset,
		"form": form,
	}
	return render(request, "data/add_items.html", context)"""






    










