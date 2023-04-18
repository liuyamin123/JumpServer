# Generated by Django 3.2.17 on 2023-04-18 09:26

from django.db import migrations


def update_remote_app_platform(apps, schema_editor):
    platform_cls = apps.get_model('assets', 'Platform')
    remote_app_host = platform_cls.objects.filter(name='RemoteAppHost').first()
    if not remote_app_host:
        return

    protocols = remote_app_host.protocols.all()
    for protocol in protocols:
        if protocol.name == 'rdp':
            protocol.primary = True
            protocol.save()
        elif protocol.name == 'ssh':
            protocol.required = True
            protocol.save()


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0115_auto_20230417_1425'),
    ]

    operations = [
        migrations.RunPython(update_remote_app_platform)
    ]
