from django.http import HttpResponse


def home(request):

    return HttpResponse('<h1> Гружу кота!!! </h1> ')
