# Generated by Django 5.1.4 on 2024-12-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_signer_document_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='last_updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signer',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]