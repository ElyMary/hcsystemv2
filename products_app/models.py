from django.db import models

class Products(models.Model):
    recordno = models.BigAutoField(auto_created=True, primary_key=True)
    productcode = models.IntegerField(unique=True)
    productname = models.CharField(max_length=255, blank=False)
    productshortname = models.CharField(max_length=10, null=True)
    productdescription = models.CharField(max_length=255, blank=False)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="Products"
        indexes = [
            models.Index(fields=['productcode'], name='productcode_idx'),
            models.Index(fields=['productcode', 'productname'], name='productcode_productnm_idx'),
        ]

class ProductsHistory(models.Model):
    recordnohist = models.BigAutoField(auto_created=True, primary_key=True)
    recordno = models.IntegerField()
    productcode = models.IntegerField()
    productname = models.CharField(max_length=255, blank=False)
    productshortname = models.CharField(max_length=10, null=True)
    productdescription = models.CharField(max_length=255, blank=False)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="ProductsHistory"
        indexes = [
            models.Index(fields=['recordno'], name='productrecordnoh_idx'),
            models.Index(fields=['productcode'], name='productcodeh_idx'),
            models.Index(fields=['productcode', 'productname'], name='productcodeh_productnmh_idx'),
        ]