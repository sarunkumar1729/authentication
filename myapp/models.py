from django.db import models

class Product(models.Model):
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      quantity = models.IntegerField()
      photo = models.ImageField(upload_to='images/')
      
      def __str__(self):
            return(self.name)