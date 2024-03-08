from django.db import models

class RoomType(models.Model):
    recordno = models.BigAutoField(auto_created=True, primary_key=True)
    roomcode = models.IntegerField(unique=True)
    roomname = models.CharField(max_length=50, blank=False)
    roomshortname = models.CharField(max_length=10, null=True)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="RoomType"
        indexes = [
            models.Index(fields=['roomcode'], name='roomcode_idx'),
            models.Index(fields=['roomcode', 'roomname'], name='roomcode_roomname_idx'),
        ]

class RoomTypeHistory(models.Model):
    recordnohist = models.BigAutoField(auto_created=True, primary_key=True)
    recordno = models.IntegerField()
    roomcode = models.IntegerField()
    roomname = models.CharField(max_length=50, blank=False)
    roomshortname = models.CharField(max_length=10, null=True)
    remarks = models.TextField(null=True)
    transactby = models.IntegerField()
    transactdate = models.DateTimeField()
    transacttype = models.CharField(max_length=10)
    class Meta:
        db_table="RoomTypeHistory"
        indexes = [
            models.Index(fields=['recordno'], name='roomrecordnoh_idx'),
            models.Index(fields=['roomcode'], name='roomcodeh_idx'),
            models.Index(fields=['roomcode', 'roomname'], name='roomcodeh_roomnmh_idx'),
        ]