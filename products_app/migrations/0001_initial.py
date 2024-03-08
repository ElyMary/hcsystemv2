# Generated by Django 5.0.2 on 2024-02-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('recordno', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('productcode', models.IntegerField()),
                ('productname', models.CharField(max_length=255)),
                ('productshortname', models.CharField(max_length=10, null=True)),
                ('productdescription', models.CharField(max_length=255)),
                ('remarks', models.TextField(null=True)),
                ('transactby', models.IntegerField()),
                ('transactdate', models.DateTimeField()),
                ('transacttype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Products',
                'indexes': [models.Index(fields=['productcode'], name='productcode_idx'), models.Index(fields=['productcode', 'productname'], name='productcode_productnm_idx')],
            },
        ),
    ]