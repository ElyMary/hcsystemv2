# Generated by Django 5.0.2 on 2024-02-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderCategory',
            fields=[
                ('recordno', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('categorycode', models.IntegerField()),
                ('providercategoryname', models.CharField(max_length=20)),
                ('providercategoryshortname', models.CharField(max_length=10, null=True)),
                ('remarks', models.TextField(null=True)),
                ('ordernumber', models.IntegerField(default=0)),
                ('transactby', models.IntegerField()),
                ('transactdate', models.DateTimeField()),
                ('transacttype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'ProviderCategory',
                'indexes': [models.Index(fields=['categorycode'], name='categorycode_idx'), models.Index(fields=['categorycode', 'providercategoryname'], name='catcode_prvdrcatnm_idx')],
            },
        ),
    ]
