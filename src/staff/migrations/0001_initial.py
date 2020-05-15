# Generated by Django 3.0.6 on 2020-05-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(choices=[('junior', 'Junior'), ('senior', 'Senior'), ('manager', 'Manager')], max_length=50)),
                ('commission', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
