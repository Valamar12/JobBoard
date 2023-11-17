from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    url = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'companies'


class Advert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    experience = models.IntegerField()
    salary = models.IntegerField()
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, through="Application")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'adverts'

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advert = models.ForeignKey("Advert", on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'applications'