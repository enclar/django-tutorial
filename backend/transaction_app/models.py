from django.db import models
import datetime

# account model
class Account(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

# transaction model
class Transaction(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=10)
    
    created = models.DateTimeField(default=datetime.datetime.now) # Must put in default value in order to seed
    updated = models.DateTimeField(default=datetime.datetime.now) # Must put in default value in order to seed
    
    def __str__(self):
        return self.name