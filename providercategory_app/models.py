from django.db import models

# Create your models here.
class ProviderCategory(models.Model):
    recordno = models.BigAutoField(auto_created=True, primary_key=True)
    categorycode = models.IntegerField(unique=True)
    providercategoryname = models.CharField(max_length=20, blank=False)
    providercategoryshortname = models.CharField(max_length=10, null=True)
    remarks = models.TextField(null=True)
    ordernumber = models.IntegerField(default=0)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="ProviderCategory"
        indexes = [
            models.Index(fields=['categorycode'], name='categorycode_idx'),
            models.Index(fields=['categorycode', 'providercategoryname'], name='catcode_prvdrcatnm_idx'),
        ]