from django.db import models

# Create your models here.
class Images(models.Model):
    # image = models.ImageField(upload_to='input/')
    original_image = models.FileField(upload_to='input/')
    e0_image = models.FileField(upload_to='e0/')
    e1_image = models.FileField(upload_to='e1/')
    e2_image = models.FileField(upload_to='e2/')
    
    class Meta:
        verbose_name_plural = "Images"
    
    def __str__(self):
        return self.image.name
