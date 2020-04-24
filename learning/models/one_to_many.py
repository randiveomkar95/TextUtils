'''
(c) learning 2020

Purpose : Learning one to many relation
'''

from django.db import models

class Mother(models.Model):
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Son(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mother = models.ForeignKey(Mother,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name
