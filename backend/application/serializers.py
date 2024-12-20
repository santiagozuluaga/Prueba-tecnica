from rest_framework import serializers
from application.models import Document, Signer

class SignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = ['id', 'token', 'name', 'email', 'status', 'external_id', 'created_at', 'last_updated_at']

class DocumentSerializer(serializers.ModelSerializer):
    signers = SignerSerializer(many=True, read_only=True, source='signer_set')

    class Meta:
        model = Document
        fields = ['id', 'open_id', 'token', 'name', 'status', 'external_id', 'created_at', 'last_updated_at', 'signers']