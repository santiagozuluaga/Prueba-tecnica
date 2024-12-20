import json
import requests

from django.core import serializers
from django.views import View
from django.http import JsonResponse

from shared.zapsign import create_document
from application.models import Document, Signer
from application.serializers import DocumentSerializer, SignerSerializer

class SignerViews(View):
    def put(self, request):
        pass