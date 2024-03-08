# Generated by Django 5.0.2 on 2024-02-27 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LimitType',
            fields=[
                ('recordno', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('limittypecode', models.IntegerField()),
                ('limittypename', models.CharField(max_length=50)),
                ('limittypeshortname', models.CharField(max_length=10)),
                ('limittypeunit', models.CharField(max_length=15)),
                ('remarks', models.TextField(null=True)),
                ('transactby', models.IntegerField()),
                ('transactdate', models.DateTimeField()),
                ('transacttype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'LimitType',
                'indexes': [models.Index(fields=['limittypecode'], name='limtypcode_idx'), models.Index(fields=['limittypecode', 'limittypename'], name='limtypcode_limtypnm_idx')],
            },
        ),
        migrations.CreateModel(
            name='LimitTypeHistory',
            fields=[
                ('recordnohist', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('recordno', models.IntegerField()),
                ('limittypecode', models.IntegerField()),
                ('limittypename', models.CharField(max_length=50)),
                ('limittypeshortname', models.CharField(max_length=10)),
                ('limittypeunit', models.CharField(max_length=15)),
                ('remarks', models.TextField(null=True)),
                ('transactby', models.IntegerField()),
                ('transactdate', models.DateTimeField()),
                ('transacttype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'LimitTypeHistory',
                'indexes': [models.Index(fields=['recordno'], name='limitrecordnoh_idx'), models.Index(fields=['limittypecode'], name='limtypcodeh_idx'), models.Index(fields=['limittypecode', 'limittypename'], name='limtypcodeh_limtypnmh_idx')],
            },
        ),
    ]
