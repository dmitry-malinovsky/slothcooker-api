# Generated by Django 2.1.10 on 2019-09-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='steps',
            field=models.ManyToManyField(to='core.Step'),
        ),
    ]
