import json
import requests

from django.db import DatabaseError
from django.http import JsonResponse
from django.views import View

from shared.zapsign import create_document

from application.models import Document, Signer
from application.serializers import DocumentSerializer, SignerSerializer

def validate_data(data):
    if "name" not in data:
        return JsonResponse(
            data={
                "http_code": 400,
                "message": "Invalid request: missing document name."
            },
            status=400,
        )
    
    if "signers" not in data:
        return JsonResponse(
            data={
                "http_code": 400,
                "message": "Invalid request: missing document signers."
            },
            status=400,
        )
    
    signers = data["signers"]

    if len(signers) == 0:
        return JsonResponse(
            data={
                "http_code": 400,
                "message": "Invalid request: missing document signers."
            },
            status=400,
        )

    for signer in signers:
        if "name" not in signer:
            return JsonResponse(
                data={
                    "http_code": 400,
                    "message": "Invalid request: missing signer name."
                },
                status=400,
            )
        
        if "email" not in signer:
            return JsonResponse(
                data={
                    "http_code": 400,
                    "message": "Invalid request: missing signer email."
                },
                status=400,
            )
        
    return None

class DocumentsViews(View):
    def get(self, request):
        try:
            documents = Document.objects.prefetch_related('signer_set').all()
            documentsSerialized = DocumentSerializer(documents, many=True).data
            return JsonResponse(
                data={
                    "documents": documentsSerialized
                },
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

    def post(self, request):
        data = None
        document = None
        
        try:
            data = json.loads(request.body)

            response = validate_data(data)
            if response != None:
                return response
        except json.JSONDecodeError as err:
            print(err)
            return JsonResponse(
                data={
                    "http_code": 400,
                    "message": "Invalid request: missing request body."
                },
                status=400,
            )
        
        try:
            document = create_document(
                api_key="",
                data=data,
            )
        except requests.exceptions.RequestException as err:
            print(err)
            return JsonResponse(
                data={
                    "http_code": 500,
                    "message": "Internal server error, try again."
                },
                status=500,
            )
        
        try:
            documentCreated = Document.objects.create(
                open_id=document["open_id"],
                token=document["token"],
                name=document["name"],
                status=document["status"],            
                external_id=document["external_id"],
            )
            documentSerialized = DocumentSerializer(documentCreated).data

            signers = []

            for signer in  document["signers"]:
                signers.append(Signer(
                    token=signer["token"],
                    name=signer["name"],
                    email=signer["email"],
                    status=signer["status"],   
                    external_id=signer["external_id"],
                    document_id=documentCreated
                ))

            signersCreated = Signer.objects.bulk_create(signers)
            signersSerialized = SignerSerializer(signersCreated, many=True).data
            documentSerialized["signers"] = signersSerialized

            return JsonResponse(
                data=documentSerialized,
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