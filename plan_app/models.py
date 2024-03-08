from django.db import models
from products_app.models import Products
from roomtype_app.models import RoomType
from membertype_app.models import MemberType
from limittype_app.models import LimitType

class Plan(models.Model):
    recordno = models.BigAutoField(auto_created=True, primary_key=True)
    plancode = models.IntegerField(unique=True)
    plantype = models.CharField(max_length=100, blank=False)
    #productcode = models.IntegerField()
    productcode = models.ForeignKey(Products, on_delete=models.DO_NOTHING, to_field='productcode')
    roomcode = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING, to_field='roomcode')
    membertypecode = models.ForeignKey(MemberType, on_delete=models.DO_NOTHING, to_field='membertypecode')
    agefrom = models.DecimalField(max_digits=18, decimal_places=6)
    ageto = models.DecimalField(max_digits=18, decimal_places=6)
    premiumamount = models.DecimalField(max_digits=18, decimal_places=6)
    benefitlimit = models.DecimalField(max_digits=18, decimal_places=6)
    limittypecode = models.ForeignKey(LimitType, on_delete=models.DO_NOTHING, to_field='limittypecode')
    withaccesstotophospital = models.IntegerField()
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="Plan"
        indexes = [
            models.Index(fields=['plancode'], name='plancode_idx'),
            models.Index(fields=['plancode', 'plantype'], name='plancode_plantype_idx'),
        ]

class PlanHistory(models.Model):
    recordnohist = models.BigAutoField(auto_created=True, primary_key=True)
    recordno = models.IntegerField()
    plancode = models.IntegerField()
    plantype = models.CharField(max_length=100, blank=False)
    #productcode = models.IntegerField()
    productcode = models.ForeignKey(Products, on_delete=models.DO_NOTHING, to_field='productcode')
    #roomcode = models.IntegerField()
    roomcode = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING, to_field='roomcode')
    #membertypecode = models.IntegerField()
    membertypecode = models.ForeignKey(MemberType, on_delete=models.DO_NOTHING, to_field='membertypecode')
    agefrom = models.DecimalField(max_digits=18, decimal_places=6)
    ageto = models.DecimalField(max_digits=18, decimal_places=6)
    premiumamount = models.DecimalField(max_digits=18, decimal_places=6)
    benefitlimit = models.DecimalField(max_digits=18, decimal_places=6)
    #limittypecode = models.IntegerField()
    limittypecode = models.ForeignKey(LimitType, on_delete=models.DO_NOTHING, to_field='limittypecode')
    withaccesstotophospital = models.IntegerField()
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="PlanHistory"
        indexes = [
            models.Index(fields=['recordno'], name='planrecordnoh_idx'),
            models.Index(fields=['plancode'], name='plancodeh_idx'),
            models.Index(fields=['plancode', 'plantype'], name='plancode_plantypeh_idx'),
        ]