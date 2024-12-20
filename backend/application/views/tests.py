from django.test import TestCase

from application.models import Document

class DocumentsViewsTest(TestCase):
    fixtures = ["documents", "signers"]

    def test_get_documents(self):
        response = self.client.get(f'/api/docs/')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data["documents"]), 2)

        documents = data["documents"]

        self.assertEqual(len(documents[0]["signers"]), 2)
        self.assertEqual(len(documents[1]["signers"]), 1)

    def test_post_document(self):
        documents = Document.objects.all()

        self.assertEqual(len(documents), 2)

        data = {
            "name": "Probando zapsign",
            "signers": [
                {
                    "name": "SANTIAGO ZULUAGA",
                    "email": "szuluaga@truora.com",
                    "external_id": ""
                }
            ],
            "external_id": ""
        }

        response = self.client.post(f'/api/docs/', data, content_type="application/json")
        self.assertEqual(response.status_code, 200)

        documents = Document.objects.all()

        self.assertEqual(len(documents), 3)

    def test_post_document_errors(self):
        data = {}

        response = self.client.post(f'/api/docs/', data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        
        data = response.json()

        self.assertEqual(data["message"], "Invalid request: missing document name.")

        data = {
            "name": "Probando zapsign",
        }

        response = self.client.post(f'/api/docs/', data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        
        data = response.json()

        self.assertEqual(data["message"], "Invalid request: missing document signers.")

        data = {
            "name": "Probando zapsign",
            "signers": []
        }

        response = self.client.post(f'/api/docs/', data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        
        data = response.json()

        self.assertEqual(data["message"], "Invalid request: missing document signers.")

        data = {
            "name": "Probando zapsign",
            "signers": [
                {

                }
            ]
        }

        response = self.client.post(f'/api/docs/', data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        
        data = response.json()

        self.assertEqual(data["message"], "Invalid request: missing signer name.")

        data = {
            "name": "Probando zapsign",
            "signers": [
                {
                    "name": "SANTIAGO ZULUAGA"
                }
            ]
        }

        response = self.client.post(f'/api/docs/', data, content_type="application/json")
        self.assertEqual(response.status_code, 400)
        
        data = response.json()

        self.assertEqual(data["message"], "Invalid request: missing signer email.")


class DocumentViewsTest(TestCase):
    fixtures = ["documents", "signers"]

    def test_get_document(self):
        response = self.client.get(f'/api/docs/1/')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["id"], 1)
        self.assertEqual(data["open_id"], 1)
        self.assertEqual(data["name"], "Probando zapsign")

    def test_get_document_errors(self):
        response = self.client.get(f'/api/docs/10/')
        self.assertEqual(response.status_code, 404)

        data = response.json()

        self.assertEqual(data["http_code"], 404)
        self.assertEqual(data["message"], "Document with id 10 not found.")

    def test_put_document(self):
        pass

    def test_delete_document(self):
        response = self.client.delete(f'/api/docs/1/')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["message"], "Document with id 1 was successfully deleted.")

    def test_delete_document_errors(self):
        response = self.client.get(f'/api/docs/10/')
        self.assertEqual(response.status_code, 404)

        data = response.json()

        self.assertEqual(data["http_code"], 404)
        self.assertEqual(data["message"], "Document with id 10 not found.")