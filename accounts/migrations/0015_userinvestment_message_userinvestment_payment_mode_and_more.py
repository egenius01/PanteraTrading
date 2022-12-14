# Generated by Django 4.1.2 on 2022-10-27 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_customuser_roi_userinvestment_roi'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinvestment',
            name='message',
            field=models.CharField(blank=True, default='Pending Approval', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userinvestment',
            name='payment_mode',
            field=models.CharField(default='Bitcoin', help_text='What Payment Method Suits You?', max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Withdrawals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(help_text='Describe Method of Payment', max_length=20)),
                ('approved', models.BooleanField()),
                ('investments', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='accounts.userinvestment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
