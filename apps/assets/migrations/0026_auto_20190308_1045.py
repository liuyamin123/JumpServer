# Generated by Django 2.1.7 on 2019-03-08 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0025_auto_20190221_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={'ordering': ['key'], 'verbose_name': 'Node'},
        ),
    ]
