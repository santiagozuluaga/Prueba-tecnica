# Generated by Django 5.1.4 on 2024-12-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_signer_created_at_signer_last_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='signer',
            name='last_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
