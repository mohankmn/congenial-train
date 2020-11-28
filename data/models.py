from django.db import models
from django.db.models.fields import SlugField
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here
class Items(models.Model):
    name =models.CharField(max_length=150)
    
    def __str__(self):
        return "{}".format(self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super().save(*args, **kwargs)

class Demand(models.Model):
    item=models.ForeignKey('Items', on_delete=models.CASCADE)
    price=models.PositiveIntegerField(blank=False,null=True)
    date=models.DateTimeField(default=timezone.now)
    quantity=models.IntegerField(default='0',blank=True,null=True)
    total=models.IntegerField(default='0',blank=True,null=True)


    def save(self,*args,**kwargs):
        self.total=(self.price)*self.quantity
        super().save(*args,**kwargs)
        
    
    def __str__(self):
        return "sold {} {} on {}".format(self.quantity,self.item.name,self.date)
    


        



    