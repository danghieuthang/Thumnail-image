from django.db import models
from PIL import Image #pip install Pillow

class ImageModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        output_size = (500,500)
        img.thumbnail(output_size)
        img.save(self.image.path)