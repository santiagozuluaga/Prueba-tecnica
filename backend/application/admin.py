from django.contrib import admin
from application.models import Company, Document, Signer

admin.site.register(
    [
        Company,
        Document,
        Signer,
    ]
)
