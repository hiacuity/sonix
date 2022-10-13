import os

import requests

MEDIA_URL = "https://api.sonix.ai/v1/media"
headers = {'Authorization': f'Bearer {API_KEY}'}


def upload_media(file):
    filename = os.path.splitext(file)
    files = {'file': open(file, 'rb').read()}
    data = {'language' : 'en'}
    requests.post(MEDIA_URL, data=data, headers=headers, files=files)


def list_media():
    media = requests.get(MEDIA_URL, headers=headers)
    results = media.json()
    for result in results['media']:
        print(result['id'])


def get_transcript(media_id):
    full_url = f"{MEDIA_URL}/{media_id}/transcript"
    transcript = requests.get(full_url, headers=headers)
    print(transcript.content)