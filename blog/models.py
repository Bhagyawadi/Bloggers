from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null= True)
    
    class Meta :
        ordering = ('-date_posted' , )
    
    def __str__(self) :
        return self.title
