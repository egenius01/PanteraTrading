# Generated by Django 3.2.15 on 2022-11-02 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_withdrawals_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawals',
            name='status',
            field=models.CharField(default='on Hold', max_length=20),
        ),
    ]
