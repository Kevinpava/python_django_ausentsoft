from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_vacation = models.BooleanField(default=False)
    date_range = models.CharField(max_length=100)
    completed_at = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title

"""
class Task(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created= models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True , blank=True)
    important= models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.title + 'by' + self.user.username
        """ 