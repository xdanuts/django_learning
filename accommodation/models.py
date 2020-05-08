from django.db import models

# Create your models here.

class Accommodation(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    def __str__(self):
        return 'Accommodation ID: {} - Name: {}'.format(self.id, self.name)


