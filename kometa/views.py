# kometa/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import requests
from kometa.models import Comets

def index(request):
    comets = Comets.objects.all()
    context = {
        'comets': comets,
    }
    return render(request, 'kometa/index.html', context)

def comet_details(request, comet_id):
    comet = get_object_or_404(Comets, pk=comet_id)
    data = {
        'name': comet.name,
        'size': comet.size,
        'color': comet.color,
        'tail': comet.tail,
    }
    return JsonResponse(data)


def index2(request):
    context = {}
    myPrompt = "Comets solar system"
    # context['text'] = myPrompt
    mycomets = Comets.objects.all().values()

    if 'comet' in request.GET:
        selectedComet = request.GET.get('comet')
        # context['selectedComet'] = selectedComet
        myComet = get_object_or_404(Comets, id=selectedComet)
        context['selectedComet'] = myComet.id

        prev_comet = mycomets.filter(id__lt=myComet.id).order_by('id').last()
        next_comet = mycomets.filter(id__gt=myComet.id).order_by('id').first()
        if prev_comet is None:
            prev_comet = mycomets.filter().order_by('id').last()
        if next_comet is None:
            next_comet = mycomets.filter().order_by('id').first()
        context['prev_comet'] = prev_comet['id']
        context['next_comet'] = next_comet['id']

        myPrompt = myComet.myprompt

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

    context['cometsList'] = mycomets
    context['imageurl'] = coded_string

    return render(request, 'kometa/index2.html', context)
