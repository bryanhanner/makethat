from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=50)
    join_date = models.DateTimeField('date joined')
    def __str__(self):
        return self.name

class Product(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.name