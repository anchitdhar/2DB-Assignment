from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    weight = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Product'
    