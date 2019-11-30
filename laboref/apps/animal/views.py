from django.http import HttpResponse


def index(request):
    return HttpResponse("App of animals.")
