from django.db import models
from django.utils import timezone
# Create your models here.
from django.db import models

class HirePost(models.Model):

    username = models.CharField(max_length=100)  
    expart_type = models.CharField(max_length=50)  
    description = models.TextField() 
    offered_money = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.username


from django.db import models

class Professional(models.Model):
    # username = models.CharField(max_length=150, unique=True) 
    username = models.CharField(max_length=150) 
    fullname = models.CharField(max_length=255)  
    profession = models.CharField(max_length=100)  
    description = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username 
