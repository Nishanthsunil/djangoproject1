from django.db import models
from django.utils.safestring import mark_safe

class movie(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(upload_to='upload')
    discription=models.TextField()
    year=models.IntegerField()
    
    def image_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width="100"/>')
    


# Create your models here.
