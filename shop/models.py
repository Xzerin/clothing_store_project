from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
