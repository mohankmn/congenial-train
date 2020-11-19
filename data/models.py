from django.db import models
from django.db.models.fields import SlugField
from django.shortcuts import reverse

# Create your models here.
class Items(models.Model):
    name =models.CharField(max_length=150, db_index=True,unique=True)
    price=models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return "{} - Price Rs. {} ".format(self.name,self.price)
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)




class Demand(models.Model):
    product=models.ForeignKey('Items', on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return "sold {} {} on {}".format(self.quantity,self.product.name,self.date)



    