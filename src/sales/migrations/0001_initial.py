# Generated by Django 3.0.6 on 2020-05-15 20:43

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('item', django.contrib.postgres.fields.jsonb.JSONField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'))),
                ('staff_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.StaffMember')),
            ],
        ),
    ]
