# from django.http import HttpResponse
# from django.utils.html import format_html
import base64
import requests
import json
#  funkcijos reikalvimai ka vartotojas daro uzrasyti juos

from django.shortcuts import render

def home(request):
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNWU2ZjEyMTAtN2YwNi00MWE5LTkxYmUtNDU2ZTQ5MzM0YzI4IiwidHlwZSI6ImFwaV90b2tlbiJ9.yoQFgst5oE-Vc9tONvODrUOYok-CkCqZLhsn-_2d6Do"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": "this is a test of Eden AI",
        "resolution": "512x512",
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['items'])

    # print(response.json())
    coded_string = result['openai']['items']
    # url = "https://imageai-generator.p.rapidapi.com/image"
    # payload = {
    #     "negative_prompt": "photo ",
    #     "prompt": "mars lion",
    #     "width": 512,
    #     "height": 512,
    #     "hr_scale": 2
    # }
    # headers = {
    #     "x-rapidapi-key": "fc336b402bmsh6135b08cfe82fe2p166b65jsnf318c4fb2156",
    #     "x-rapidapi-host": "imageai-generator.p.rapidapi.com",
    #     "Content-Type": "application/json"
    # }

    # response = requests.post(url, json=payload, headers=headers)
    # coded_string = response.json()
    # # print(coded_string)
    blocks = {'imageurl': coded_string}
    return render(request, "getimage/index.html", blocks)
