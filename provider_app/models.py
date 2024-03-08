from django.db import models

# Create your models here.
class Providers(models.Model):
    recordno = models.BigAutoField(auto_created=True, primary_key=True)
    providercode = models.IntegerField(unique=True)
    categorycode = models.IntegerField(blank=False)
    providername = models.CharField(max_length=255, blank=False)
    tin = models.CharField(max_length=20, default="")
    address = models.CharField(max_length=255, null=True)
    emailaddress = models.EmailField(max_length=50, null=True)
    locationcode = models.IntegerField()
    contactperson = models.CharField(max_length=255, null=True)
    landline = models.CharField(max_length=150, null=True)
    mobilenumber = models.CharField(max_length=150, null=True)
    remarks = models.TextField(null=True)
    # percentage = models.DecimalField(max_digits=18, decimal_places=6, default=0)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="Providers"
        indexes = [
            models.Index(fields=['providercode'], name='providercode_idx'),
            models.Index(fields=['providercode', 'providername'], name='prvdrcode_prvdrnm_idx'),
        ]