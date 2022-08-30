# Generated by Django 3.1.14 on 2022-04-30 14:41

from collections import namedtuple
from django.db import migrations, models
import django.db.models.deletion


def migrate_platform_set_ops(apps, *args):
    platform_model = apps.get_model('assets', 'Platform')

    default_ok = {
        'su_enabled': True,
        'su_method': 'sudo',
        'domain_enabled': True,
        'change_password_enabled': True,
        'change_password_method': 'change_password_linux',
        'verify_account_enabled': True,
        'verify_account_method': 'verify_account_ansible',
    }

    platform_ops_map = {
        'Linux': {**default_ok, 'change_password_method': 'change_password_linux'},
        'Windows': {**default_ok, 'change_password_method': 'change_password_windows'},
        'AIX': {**default_ok, 'change_password_method': 'change_password_aix'},
    }
    platforms = platform_model.objects.all()

    for p in platforms:
        p.set_ops = True
        p.save()


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0097_auto_20220426_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformProtocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('port', models.IntegerField(verbose_name='Port')),
                ('setting', models.JSONField(default=dict, verbose_name='Setting')),
            ],
        ),
        migrations.AddField(
            model_name='platform',
            name='domain_default',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.domain', verbose_name='Domain default'),
        ),
        migrations.AddField(
            model_name='platform',
            name='domain_enabled',
            field=models.BooleanField(default=True, verbose_name='Domain enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='protocols_enabled',
            field=models.BooleanField(default=True, verbose_name='Protocols enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='protocols',
            field=models.ManyToManyField(blank=True, to='assets.PlatformProtocol', verbose_name='Protocols'),
        ),
        migrations.AddField(
            model_name='platform',
            name='change_password_enabled',
            field=models.BooleanField(default=False, verbose_name='Change password enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='change_password_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Change password method'),
        ),
        migrations.AddField(
            model_name='platform',
            name='create_account_enabled',
            field=models.BooleanField(default=False, verbose_name='Create account enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='create_account_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Create account method'),
        ),
        migrations.AddField(
            model_name='platform',
            name='ping_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='platform',
            name='ping_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Ping method'),
        ),
        migrations.AddField(
            model_name='platform',
            name='su_enabled',
            field=models.BooleanField(default=False, verbose_name='Su enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='su_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='SU method'),
        ),
        migrations.AddField(
            model_name='platform',
            name='verify_account_enabled',
            field=models.BooleanField(default=False, verbose_name='Verify account enabled'),
        ),
        migrations.AddField(
            model_name='platform',
            name='verify_account_method',
            field=models.TextField(blank=True, max_length=32, null=True, verbose_name='Verify account method'),
        ),
    ]
