from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_ID = models.IntegerField(primary_key=True)
    PRODUCT_NAME = models.CharField(max_length=100)
    PRODUCT_CATEGORY = models.CharField(max_length=100)
    COST_PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    SELLING_PRICE = models.DecimalField(max_digits=10, decimal_places=2)
    SALES_DATA = models.IntegerField()
    QUANTITY_SOLD = models.IntegerField()
    SEASON = models.CharField(max_length=100)
    PROFIT_MARGIN = models.CharField(max_length=100)
    RATING = models.DecimalField(max_digits=3, decimal_places=1)
    SPACE_OCCUPIED = models.IntegerField()
    NO_OF_DAYS_LEFT = models.IntegerField()

    def __str__(self):
        return self.PRODUCT_NAME
    

    # PRODUCT_ID = models.IntegerField(primary_key=True)
    # PRODUCT_NAME = models.CharField(max_length=100)
    # PRODUCT_CATEGORY = models.CharField(max_length=100)
    # COST_PRICE = models.DecimalField(max_digits=8, decimal_places=2)
    # SELLING_PRICE = models.DecimalField(max_digits=8, decimal_places=2)
    # SALES_DATA = models.IntegerField()
    # QUANTITY_SOLD = models.IntegerField()
    # SEASON = models.CharField(max_length=20)
    # PROFIT_MARGIN = models.CharField(max_length=10)
    # RATING = models.DecimalField(max_digits=3, decimal_places=1)
    # SPACE_OCCUPIED = models.IntegerField()
    # NO_OF_DAYS_LEFT = models.IntegerField()