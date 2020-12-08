import math
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg, StdDev,Sum,Variance
from django.db.models.expressions import F
from django.shortcuts import get_object_or_404, render
from numpy.core.fromnumeric import product
from .models import Items,Demand
import pandas as pd
import numpy as np
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
    total=None

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
    return render(request,'data/items_list.html',context = {"form": form,"items":ite,"total":total})


@login_required(login_url='login')
def demand_list(request,*args,**kwargs):
    demand=Demand.objects.all()
    return render(request,'data/demand_list.html',context={'demand':demand})


@login_required(login_url='login')
def DemandCreate(request):
        form=DemandForm(user=request.user)
        if request.method == 'POST':
            form=DemandForm(request.POST) 
            if form.is_valid():
                n = form.cleaned_data["item"]
                l = form.cleaned_data["issue_quantity"]
                c = form.cleaned_data["price"]
                o = form.cleaned_data["recieve_quantity"]
                d = form.cleaned_data["date"]

                reporter = Items.objects.get(name=n)
                reporter.total_inventory = F('total_inventory')-l+o
                reporter.save()
                t = Demand(item=n,issue_quantity=l,price=c,recieve_quantity=o,date=d)
                t.save()

                return redirect('data:demand_create_url')
                    
        return render(request,'data/demand_create.html',context={'form':form })


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
                t = form.cleaned_data["total_inventory"]
                u = form.cleaned_data["unit_costprice"]
                s = form.cleaned_data["service_level"]
                w = form.cleaned_data["no_of_workingdays"]
                d = form.cleaned_data["standard_deviation"]
                a = form.cleaned_data["average_daily_demand"]

                for i in request.user.items.all():
                    if i.name==n:
                        messages.error(request, n +' Item Already Created')
                        return redirect('data:item_create_url')


                

                t = Items(name=n,lead_time=l,average_daily_demand=a,carrying_cost=c,ordering_cost=o,total_inventory=t,unit_costprice=u,service_level=s,no_of_workingdays=w,standard_deviation=d)
                t.save()
                request.user.items.add(t) 
                messages.success(request, n +' Item Created')
                return redirect('data:items_list_url')
                    
        return render(request,'data/item_create.html',context={'form':form })



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

def calculations(request):
    item_df=pd.DataFrame(Items.objects.all().values())
    demand_df=pd.DataFrame(Demand.objects.all().values())
    item_df['item_id']=item_df['id']
    df=pd.merge(item_df,demand_df,on='item_id').drop(['user_id','id_y','id_x','carrying_cost','ordering_cost','unit_costprice','yearly_demand'],axis=1).rename({'item_id':'id'},axis=1)
    df1=df.groupby(['name']).aggregate({'issue_quantity':['var','mean'],'lead_time':'mean','total_inventory':'mean','eoq':'mean','z':'mean'})
    df1['Reorder Quantity']=(df1['issue_quantity']['mean']*df1['lead_time']['mean'])+((np.sqrt(df1['issue_quantity']['var']*df1['lead_time']['mean']))*df1['z']['mean'])
    del df1['issue_quantity']
    del df1['lead_time']
    df1.rename(columns = {'total_inventory':'Inventory Left'}, inplace = True) 
    df1.rename(columns = {'mean':''}, inplace = True) 
    df1.rename(columns = {'':''}, inplace = True) 
    df1.rename(columns = {'eoq':'EOQ'}, inplace = True) 
    df1.rename(columns = {'name':'Item Name'}, inplace = True) 
    context={
        'df1':df1.to_html,
    }
    return render(request,'data/calculations.html',context)


"""def view(response):
    return render(response, "data/view.html", {})"""
	
	



"""def issue_items(request, pk):
    queryset = Items.objects.get(id=pk)
    form=IssueForm()

    if request.method=='POST':
        form=IssueForm(request.POST,instance=queryset)
        if form.is_valid():
            queryset.total_inventory -= queryset.issue_quantity
            form.save()

            return redirect('data:items_list_url')
    context = {"queryset":queryset,"form":form}
    return render(request, "data/add_items.html", context)"""

"""def add_inventory(request, pk):
    queryset = Items.objects.get(id=pk)
    form=IssueForm()

    if request.method=='POST':
        form=IssueForm(request.POST,instance=queryset)
        if form.is_valid():
            queryset.total_inventory += queryset.issue_quantity
            form.save()

            return redirect('data:items_list_url')
    context = {"queryset":queryset,"form":form}
    return render(request, "data/add_inventory.html", context)"""







    



