from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField(default=0)
    join_date = models.DateTimeField('date joined')
    def __str__(self):
        return self.username

class Product(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.name