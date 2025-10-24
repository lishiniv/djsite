from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.
def index(request):
    # template = render_to_string('women/index.html')
    # return HttpResponse(template)
    data = {'title': 'Главная страница'}
    return render(request, 'women/index.html', data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def cats(request, cat_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статья по категориям</h1><p>{cat_id}</p>")


def categories(request, cat_slug):
    return HttpResponse(f"<h1>Статья по категориям</h1><p>cat_slug: {cat_slug}</p>")


def archive(request, year):
    if int(year) > 2025:
        url = reverse('categories', args=('music',))
        return HttpResponsePermanentRedirect(url)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
