# Generated by Django 4.1.2 on 2022-10-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_customuser_created_customuser_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='roi',
        ),
        migrations.AddField(
            model_name='userinvestment',
            name='roi',
            field=models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('BI-WEEKLY', 'Bi-Weekly')], default='DAILY', max_length=20),
        ),
    ]
