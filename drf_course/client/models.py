from django.db import models

# Create your models here.


class Client(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    def __repr__(self):
        return 'Image(%s, %s)' % (self.first_name, self.last_name)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

