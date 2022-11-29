# Generated by Django 3.2.14 on 2022-11-29 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0113_alter_accounttemplate_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='domain',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                related_name='nodes', to='assets.domain', verbose_name='Domain'
            ),
        ),
    ]
