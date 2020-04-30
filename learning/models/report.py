'''
(c) learning 2020

Purpose : Learning one to many relation
'''

from django.db import models

class Detail(models.Model):
    name = models.CharField(max_length=100,unique=True)
    type = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Status(models.Model):
    started_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25)
    detail = models.ForeignKey(Detail, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.detail)
