from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse


# Create your views here.
def figurere(request, figure: str):
    if figure in ('rectangle', 'square', 'circle'):
        return render(request, f'geometry/{figure}.html')
    else:
        return HttpResponseBadRequest


def get_rectangle_area(request, width: int, height: int):
    redirect_url = reverse('figure-r', args=(width, height))
    return HttpResponseRedirect(redirect_url)


#
def get_square_area(request, width: int):
    redirect_url = reverse('figure-s', args=(width,))
    return HttpResponseRedirect(redirect_url)


def get_circle_area(request, radius: int):
    redirect_url = reverse('figure-c', args=(radius,))
    return HttpResponseRedirect(redirect_url)


def rectangle(request, width: int, height: int):
    return HttpResponse(f'Площадь прямугольника размером {width}x{height} равна {width * height}')


def square(request, width: int):
    return HttpResponse(f'Площадь квадрата {width}x{width} равна {width ** 2}')


def circle(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равен {round(radius ** 2 * 3.14, 1)}')
