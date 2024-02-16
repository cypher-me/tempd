from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class CharityItem(models.Model):
    charity_title = models.CharField(max_length=255)
    charity_short_description = models.TextField()
    charity_long_description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.charity_title

    
