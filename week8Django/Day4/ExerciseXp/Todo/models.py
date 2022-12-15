from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15, blank=True)
    image=models.URLField(blank=True)
    def __str__(self):
        return self.name
class Todo(models.Model):
    title = models.CharField(max_length=15,blank=True)
    details = models.TextField(default='')
    date_creation = models.DateTimeField(auto_now = True)
    date_completion =models.DateTimeField(null=True,blank=True )
    deadline_date =models.DateTimeField()
    has_been_done =models.BooleanField(default=False)
    category = models.ForeignKey(Category,   on_delete=models.CASCADE)
    def __str__(self):
        return self.title