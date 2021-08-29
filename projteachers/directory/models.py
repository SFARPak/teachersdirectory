import random
from django.db import models
from django.utils.text import slugify

class Teacher(models.Model):
    
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=120)
    room_no = models.CharField(max_length=10)
    image = models.ImageField(upload_to='static/images/teachers/', null=True, blank=True)
    slug = models.SlugField(max_length=230, blank=True)
    subject = models.CharField(max_length=120)
    
    # def save(self, *args, **kwargs):
    #     if self.slug is None:
    #         self.slug = slugify(self.first_name)
    #     super().save(*args, **kwargs)

    def __str__ (self):
        return f'{self.first_name} {self.last_name}' 

    def get_absolute_url(self):
         return f"/teacher/{self.slug}"

    def get_edit_url(self):
        return f"/teacher/{self.slug}/edit"
    
    def get_delete_url(self):
        return f"/teacher/{self.slug}/delete"