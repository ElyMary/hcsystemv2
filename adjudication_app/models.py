from django.db import models

# Create your models here.

class Adjudication(models.Model):
    recordnoadju = models.BigAutoField(auto_created=True, primary_key=True)
    adjudicationcode = models.IntegerField(unique=True)
    providercode = models.IntegerField()
    soanumber = models.IntegerField()
    soadate = models.DateField()
    duedate = models.DateField()
    claimsstatus = models.CharField(max_length=50)
    remarks = models.TextField()
    transactby =  models.IntegerField()
    transactdate = models.DateTimeField()
    transactype = models.CharField(max_length=50)
    
    class Meta:
        db_table = "Adjudication"
        indexes = [
            models.Index(fields=['adjudicationcode'], name='adjudicationcode_idx'),
            models.Index(fields=['duedate'], name='duedate_idx')
        ]
    

