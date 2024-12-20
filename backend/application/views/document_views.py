import json
from django.db import DatabaseError
from django.http import JsonResponse
from django.views import View

from application.models import Document, Signer
from application.serializers import DocumentSerializer

class DocumentViews(View):
    def get(self, request, document_id):
        try:
            document = Document.objects.get(pk=document_id)
            documentSerialized = DocumentSerializer(document).data

            return JsonResponse(
                data=documentSerialized,
            )
        except Document.DoesNotExist:
            return JsonResponse(
                data={
                    "http_code": 404,
                    "message": f"Document with id {document_id} not found.",
                },
                status=404,
            )
        except DatabaseError as err:
            print(err)
            return JsonResponse(
                data={
                    "http_code": 500,
                    "message": "Internal server error, try again."
                },
                status=500,
            )

    def put(self, request, document_id):
        data = None
        
        try:
            data = json.loads(request.body)

            Document.objects.filter(pk=document_id).update(
                name=data["name"],
                external_id=data["external_id"],
            )

            signers = data.get('signers', [])
            for signer in signers:
                Signer.objects.filter(pk=signer["id"]).update(
                    name=signer["name"],
                    email=signer["email"],
                    external_id=signer["external_id"],
                )
                
            return JsonResponse(
                data={
                    "message": f"Document with id {document_id} was successfully updated.",
                },
            )
        except json.JSONDecodeError as err:
            print(err)
            return JsonResponse(
                data={
                    "http_code": 400,
                    "message": "Invalid request: missing request body."
                },
                status=400,
            )

    def delete(self, request, document_id):
        try:
            document = Document.objects.get(pk=document_id)
            document.delete()
            return JsonResponse(
                data={
                    "message": f"Document with id {document_id} was successfully deleted.",
                },
            )
        except Document.DoesNotExist:
            return JsonResponse(
                data={
                    "http_code": 404,
                    "message": f"Document with id {document_id} not found.",
                },
                status=404,
            )
        except DatabaseError as err:
            print(err)
            return JsonResponse(
                data={
                    "http_code": 500,
                    "message": "Internal server error, try again."
                },
                status=500,
            )