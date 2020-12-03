from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models her
class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="items")
    name =models.CharField(max_length=150)
    lead_time=models.PositiveIntegerField(default='0',blank=True,null=True)
    carrying_cost=models.PositiveIntegerField(default='0',blank=True,null=True)
    ordering_cost=models.PositiveIntegerField(default='0',blank=True,null=True)
    
    def __str__(self):
        return "{}".format(self.name)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        return super().save(*args, **kwargs)

class Demand(models.Model):
    item=models.ForeignKey('Items', on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default='0',blank=True,null=True)
    date=models.DateTimeField(default=timezone.now)
    quantity=models.IntegerField(default='0',blank=True,null=True)
    total=models.IntegerField(default='0',blank=True,null=True)


    def save(self,*args,**kwargs):
        self.total=(self.price)*self.quantity
        super().save(*args,**kwargs)
        
    
    def __str__(self):
        return "sold {} {} on {}".format(self.quantity,self.item.name,self.date)
    


        



    