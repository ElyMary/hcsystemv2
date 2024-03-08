# Generated by Django 5.0.2 on 2024-02-27 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('recordno', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('membertypecode', models.IntegerField()),
                ('membertypename', models.CharField(max_length=50)),
                ('membertypeshortname', models.CharField(max_length=10, null=True)),
                ('remarks', models.TextField(null=True)),
                ('transactby', models.IntegerField()),
                ('transactdate', models.DateTimeField()),
                ('transacttype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'MemberType',
                'indexes': [models.Index(fields=['membertypecode'], name='mmbrtypcode_idx'), models.Index(fields=['membertypecode', 'membertypename'], name='mmbrtypcode_mmbrtypnm_idx')],
            },
        ),
        migrations.CreateModel(
            name='MemberTypeHistory',
            fields=[
                ('recordnohist', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('recordno', models.IntegerField()),
                ('membertypecode', models.IntegerField()),
                ('membertypename', models.CharField(max_length=50)),
                ('membertypeshortname', models.CharField(max_length=10, null=True)),
                ('remarks', models.TextField(null=True)),
                ('transactby', models.IntegerField()),
                ('transactdate', models.DateTimeField()),
                ('transacttype', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'MemberTypeHistory',
                'indexes': [models.Index(fields=['recordno'], name='mmbrtyprecordnoh_idx'), models.Index(fields=['membertypecode'], name='mmbrtypcodeh_idx'), models.Index(fields=['membertypecode', 'membertypename'], name='mmbrtypcodeh_mmbrtypnmh_idx')],
            },
        ),
    ]