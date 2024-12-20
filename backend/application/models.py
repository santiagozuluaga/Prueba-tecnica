from django.db import models

class Company(models.Model):
    class Meta:
        verbose_name_plural = "Companies"
    name = models.CharField(max_length=255)
    api_token = models.CharField(max_length=255)

class Document(models.Model):
    class Meta:
        ordering = ["-created_at"]
    open_id = models.IntegerField()
    token = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    external_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

class Signer(models.Model):
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    external_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
                                           
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)