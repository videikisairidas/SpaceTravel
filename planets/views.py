from django.shortcuts import render
from planets.models import Planets, Objects
import requests
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    context = {}
    myPrompt = "Our solar system Sun. Realistic photo"
    myplanets = Planets.objects.all().values()
    

    if 'planet' in request.GET:
        selectedPlanet = request.GET.get('planet')
        context['selectedPlanet'] = selectedPlanet
        myPlanet = get_object_or_404(Planets, name=selectedPlanet)

        prev_planet = myplanets.filter(id__lt=myPlanet.id).order_by('id').last()
        next_planet = myplanets.filter(id__gt=myPlanet.id).order_by('id').first()
        if prev_planet is None:
            prev_planet = myplanets.filter().order_by('id').last()
        if next_planet is None:
            next_planet = myplanets.filter().order_by('id').first()
        context['prev_planet'] = prev_planet['name']
        context['next_planet'] = next_planet['name']

        context['text'] = myPlanet.content
        context['objects'] = Objects.objects.filter(planetID=myPlanet.id).values()

        myPrompt = myPlanet.content


        if 'objectID' in request.GET:
            urlObject = request.GET.get('objectID')
            mySelectObject = Objects.objects.get(id=urlObject)
            context['selectedObject'] = mySelectObject.id
            context['text'] = mySelectObject.content

            prev_object = context['objects'].filter(id__lt=urlObject).order_by('id').last()
            next_object = context['objects'].filter(id__gt=urlObject).order_by('id').first()
            if prev_object is None:
                prev_object = context['objects'].filter().order_by('id').last()
            if next_object is None:
                next_object = context['objects'].filter().order_by('id').first()

            context['prev_object'] = prev_object['id']
            context['next_object'] = next_object['id']
            context['prev_planet'] = myPlanet.name
            context['next_planet'] = myPlanet.name
            myPrompt = mySelectObject.content


    # rapidapi
    context['text'] = myPrompt
    myPrompt += "A high-resolution photograph"
    # context['text'] = myPrompt
    url = "https://imageai-generator.p.rapidapi.com/image"
    payload = {
        "negative_prompt": "cartoon drawing illustration abstract",
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

    context['planetsList'] = myplanets
    context['imageurl'] = coded_string

    return render(request, 'planets/index.html', context)


# def planet(request, planet):

#     context = {
#         # 'planetsList': myplanets,
#         # 'imageurl': coded_string,
#     }
#     return render(request, 'planets/planet.html', context)