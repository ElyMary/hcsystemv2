from django.db import models

class MemberType(models.Model):
    recordno = models.BigAutoField(auto_created=True, primary_key=True)
    membertypecode = models.IntegerField(unique=True)
    membertypename = models.CharField(max_length=50, blank=False)
    membertypeshortname = models.CharField(max_length=10, null=True)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="MemberType"
        indexes = [
            models.Index(fields=['membertypecode'], name='mmbrtypcode_idx'),
            models.Index(fields=['membertypecode', 'membertypename'], name='mmbrtypcode_mmbrtypnm_idx'),
        ]

class MemberTypeHistory(models.Model):
    recordnohist = models.BigAutoField(auto_created=True, primary_key=True)
    recordno = models.IntegerField()
    membertypecode = models.IntegerField()
    membertypename = models.CharField(max_length=50, blank=False)
    membertypeshortname = models.CharField(max_length=10, null=True)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="MemberTypeHistory"
        indexes = [
            models.Index(fields=['recordno'], name='mmbrtyprecordnoh_idx'),
            models.Index(fields=['membertypecode'], name='mmbrtypcodeh_idx'),
            models.Index(fields=['membertypecode', 'membertypename'], name='mmbrtypcodeh_mmbrtypnmh_idx'),
        ]