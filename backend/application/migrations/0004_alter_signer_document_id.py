# Generated by Django 5.1.4 on 2024-12-19 06:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_document_status_signer_document_id_signer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signer',
            name='document_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='application.document'),
        ),
    ]
