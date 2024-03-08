from django.db import models

class LimitType(models.Model):
    recordno = models.BigAutoField(auto_created=True, primary_key=True)
    limittypecode = models.IntegerField(unique=True)
    limittypename = models.CharField(max_length=50, blank=False)
    limittypeshortname = models.CharField(max_length=10, blank=False)
    limittypeunit = models.CharField(max_length=15, blank=False)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="LimitType"
        indexes = [
            models.Index(fields=['limittypecode'], name='limtypcode_idx'),
            models.Index(fields=['limittypecode', 'limittypename'], name='limtypcode_limtypnm_idx'),
        ]

class LimitTypeHistory(models.Model):
    recordnohist = models.BigAutoField(auto_created=True, primary_key=True)
    recordno = models.IntegerField()
    limittypecode = models.IntegerField()
    limittypename = models.CharField(max_length=50, blank=False)
    limittypeshortname = models.CharField(max_length=10, blank=False)
    limittypeunit = models.CharField(max_length=15, blank=False)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="LimitTypeHistory"
        indexes = [
            models.Index(fields=['recordno'], name='limitrecordnoh_idx'),
            models.Index(fields=['limittypecode'], name='limtypcodeh_idx'),
            models.Index(fields=['limittypecode', 'limittypename'], name='limtypcodeh_limtypnmh_idx'),
        ]