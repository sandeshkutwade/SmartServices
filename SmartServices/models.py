from datetime import timezone
from email.policy import default
from turtle import mode
from django.db import models
from django.db import models
from django.db.models.expressions import F
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    Name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('SmartServices:category_list', args=[self.slug])

    def __str__(self):
        return self.Name


class Partners(models.Model):
    category = models.ForeignKey(
        Category, related_name='partner', on_delete=models.CASCADE)
    # created_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='Partner_maker',default='Admin')
    
    Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255, default='Sangli')
    Contact = models.CharField(max_length=15, null=False, unique=True)
    Alternate_Contact = models.CharField(max_length=15, null=False, unique=True)

    image = models.ImageField(upload_to='images/', default='images/SSDefault.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    OtherExpertise = models.CharField(max_length=255, default="None")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'partner'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("SmartServices:worker_details", args=[self.slug])

    def __str__(self):
        return self.Name

class Order(models.Model):
    Name = models.CharField(max_length=250)
    Email = models.EmailField(max_length=255)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=250)                      
    Date = models.DateTimeField(auto_now_add=True)
    Ammount = models.CharField(max_length=100) 
    WokerName = models.CharField(max_length=555)
    
    class Meta:
        verbose_name_plural = 'Order'
    
    def __str__(self):
        return self.Name
