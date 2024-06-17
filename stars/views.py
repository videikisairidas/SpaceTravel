# kometa/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from stars.models import Stars
import requests

def index(request):
    stars = Stars.objects.all()
    context = {
        'stars': stars,
    }
    return render(request, 'stars/index.html', context)

def star_details(request, star_id):
    star = get_object_or_404(Stars, pk=star_id)
    data = {
        'name': star.name,
        'size': star.size,
        'color': star.color,
        'temperature': star.temperature,
    }
    return JsonResponse(data)



def index2(request):
    context = {}
    myPrompt = "Stars galaxy"
    # context['text'] = myPrompt
    mystars = Stars.objects.all().values()

    if 'star' in request.GET:
        selectedStar = request.GET.get('star')
        myStar = get_object_or_404(Stars, id=selectedStar)
        context['selectedStar'] = myStar.id

        prev_star = mystars.filter(id__lt=myStar.id).order_by('id').last()
        next_star = mystars.filter(id__gt=myStar.id).order_by('id').first()
        if prev_star is None:
            prev_star = mystars.filter().order_by('id').last()
        if next_star is None:
            next_star = mystars.filter().order_by('id').first()
        context['prev_star'] = prev_star['id']
        context['next_star'] = next_star['id']

        myPrompt = myStar.myprompt

    # rapidapi
    context['text'] = myPrompt
    url = "https://imageai-generator.p.rapidapi.com/image"
    payload = {
        "negative_prompt": "white",
        "prompt": myPrompt,
        "width": 512,
        "height": 512,
        "hr_scale": 2
    }
    headers = {
        "x-rapidapi-key": "fc336b402bmsh6135b08cfe82fe2p166b65jsnf318c4fb2156",
        "x-rapidapi-host": "imageai-generator.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    coded_string = response.json()

    context['starsList'] = mystars
    context['imageurl'] = coded_string

    return render(request, 'stars/index2.html', context)
