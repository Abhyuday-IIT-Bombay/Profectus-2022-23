# Generated by Django 3.0 on 2022-05-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20220525_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='make_resume',
            name='techskill',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
