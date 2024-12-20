import requests
import uuid
from shared.env import getEnvString

ZAPSIGN_API_URL = getEnvString("ZAPSIGN_API_URL", "https://sandbox.api.zapsign.com.br/api/v1/docs/")
ZAPSIGN_API_TOKEN = getEnvString("ZAPSIGN_API_TOKEN", "")

def create_document(
    api_key = None,
    data = None
):
    headers = {
        'content-type': 'application/json',
        'Authorization': 'Bearer ' + ZAPSIGN_API_TOKEN
    }
    
    response = requests.post(
        url=ZAPSIGN_API_URL,
        json=data,
        headers=headers,
    )

    response.raise_for_status()
    
    return response.json()

    