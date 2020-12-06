from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import math

# Create your models here


class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="items")
    name =models.CharField(max_length=150)
    lead_time=models.PositiveIntegerField(default='0',blank=True,null=True)
    carrying_cost=models.PositiveIntegerField(default='0',blank=False,null=True)
    ordering_cost=models.PositiveIntegerField(default='0',blank=False,null=True)
    unit_costprice=models.PositiveIntegerField(blank=False,null=True)
    yearly_demand=models.PositiveIntegerField(blank=False,null=True)
    total_inventory=models.IntegerField(default='0',blank=True,null=True)
    eoq=models.IntegerField(default='0',blank=True,null=True)
    
    
    def __str__(self):
        return "{}".format(self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.eoq = math.sqrt((2*self.yearly_demand*self.ordering_cost)/(self.unit_costprice*self.carrying_cost))
        return super().save(*args, **kwargs)

    





class Demand(models.Model):
    item=models.ForeignKey('Items', on_delete=models.CASCADE,related_name="demands")
    issue_quantity=models.IntegerField(blank=False,null=True)
    price=models.PositiveIntegerField(blank=False,null=True)
    recieve_quantity=models.IntegerField(default='0',blank=False,null=True)
    date=models.DateField(auto_now_add=True)


        
    
    def __str__(self):
        return "sold {} {} on {}".format(self.issue_quantity,self.item.name,self.date)
    


        



    