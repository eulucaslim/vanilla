from django.db import models

class Product(models.Model):
  code_product = models.IntegerField(default=0, null=False, blank=False, primary_key=True)
  name_product = models.CharField(max_length=100, default='', null=False, blank=False)
  description = models.CharField(max_length=100, default='', null=False, blank=False)
  price = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False)
  quant = models.IntegerField(default=0, null=False, blank=False)

  def __str__(self):
    return f"Product: {self.name_product} | Price: {self.price}"
