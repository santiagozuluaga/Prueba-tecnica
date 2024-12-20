from django.urls import path

from application.views.document_views import DocumentViews
from application.views.documents_views import DocumentsViews
from application.views.signer_views import SignerViews

urlpatterns = [
    path('docs/', DocumentsViews.as_view()),
    path('docs/<int:document_id>/', DocumentViews.as_view()),
    path('docs/<int:document_id>/signers/<int:signer_id>', SignerViews.as_view()),
]
