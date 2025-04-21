from django.db import models

# Create your models here.
class List(models.Model):
    text = models.TextField(default='')
    class Meta:
        db_table = 'lists'

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, null=True,blank=True, on_delete=models.CASCADE)

