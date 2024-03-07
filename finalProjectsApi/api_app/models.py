from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, blank=True)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    flow_diagram = models.ImageField(upload_to='flow_diagrams/', blank=True)
    abstract = models.TextField(blank=True)
    documentation = models.FileField(upload_to='project_documentation/', blank=True)
    video_link = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Transaction(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
