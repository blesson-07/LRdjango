from django.db import models

# Create your models here.

class user(models.Model):
    note = models.IntegerField()
    date = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    