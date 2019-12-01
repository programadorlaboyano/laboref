from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Animal


def index(request):
    animal_list = Animal.objects.all()
    template = loader.get_template('animal/index.html')
    context = {
        'animal_list': animal_list,
    }
    return HttpResponse(template.render(context, request))


def detail_animal(request, animal_id):
    animal = get_object_or_404(Animal, pk=animal_id)
    return render(request, "animal/detail.html", {'animal': animal})


