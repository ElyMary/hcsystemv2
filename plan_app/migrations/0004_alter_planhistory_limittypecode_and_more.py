# Generated by Django 5.0 on 2024-03-06 03:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limittype_app', '0004_delete_claims'),
        ('membertype_app', '0002_alter_membertype_membertypecode'),
        ('plan_app', '0003_alter_plan_plancode'),
        ('products_app', '0004_alter_products_productcode'),
        ('roomtype_app', '0003_alter_roomtype_roomcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planhistory',
            name='limittypecode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='limittype_app.limittype', to_field='limittypecode'),
        ),
        migrations.AlterField(
            model_name='planhistory',
            name='membertypecode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='membertype_app.membertype', to_field='membertypecode'),
        ),
        migrations.AlterField(
            model_name='planhistory',
            name='productcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products_app.products', to_field='productcode'),
        ),
        migrations.AlterField(
            model_name='planhistory',
            name='roomcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roomtype_app.roomtype', to_field='roomcode'),
        ),
    ]
