import os
import requests
import json

CONTENTFUL_SPACE_ID = os.getenv('CONTENTFUL_SPACE_ID')
CONTENTFUL_MANAGEMENT_ACCESS_TOKEN = os.getenv('CONTENTFUL_MANAGEMENT_ACCESS_TOKEN')
CONTENTFUL_ENVIRONMENT_ID = os.getenv('CONTENTFUL_ENVIRONMENT_ID')

def create_content_model(model_data):
    url = f"https://api.contentful.com/spaces/{CONTENTFUL_SPACE_ID}/environments/{CONTENTFUL_ENVIRONMENT_ID}/content_types"

    headers = {
        "Authorization": f"Bearer {CONTENTFUL_MANAGEMENT_ACCESS_TOKEN}",
        "Content-Type": "application/vnd.contentful.management.v1+json",
    }

    response = requests.post(url, headers=headers, data=json.dumps(model_data))

    if response.status_code == 201:
        content_type_id = response.json()['sys']['id']
        return content_type_id
    else:
        print("Error:", response.status_code, response.text)

def activate_content_model(content_type_id):
    activate_url = f"https://api.contentful.com/spaces/{CONTENTFUL_SPACE_ID}/environments/{CONTENTFUL_ENVIRONMENT_ID}/content_types/{content_type_id}/published"

    headers = {
        "Authorization": f"Bearer {CONTENTFUL_MANAGEMENT_ACCESS_TOKEN}",
        "Content-Type": "application/vnd.contentful.management.v1+json",
        "X-Contentful-Version": "1"
    }

    activate_response = requests.put(activate_url, headers=headers)

    if not activate_response.status_code == 200:
        print("Error:", activate_response.status_code, activate_response.text)

if __name__ == "__main__":
    model_data = {
        "name": "Additional Page",
        "fields": [
            {
                "id": "menu_title",
                "name": "Menu Title",
                "type": "Text"
            },
            {
                "id": "heading_text",
                "name": "Heading Text",
                "type": "Text"
            },
            {
                "id": "hero_title1",
                "name": "Hero Title 1",
                "type": "Text"
            },
            {
                "id": "hero_image1",
                "name": "Hero Image 1",
                "type": "Link",
                "linkType": "Asset"
            },
            {
                "id": "hero_title2",
                "name": "Hero Title 2",
                "type": "Text"
            },
            {
                "id": "hero_image2",
                "name": "Hero Image 2",
                "type": "Link",
                "linkType": "Asset"
            },
        ]
    }

    content_type_id = create_content_model(model_data)
    activate_content_model(content_type_id)

    print("content_type_id: ", content_type_id)
