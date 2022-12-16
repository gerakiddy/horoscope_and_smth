from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
calendar = {'monday': 'На понедельник запланировано\nНихуя не делать',
            'tuesday': 'На вторник можно просто хуй положить',
            'wednesday': 'Среда - пизда',
            'thursday': 'четверг-хуетверг',
            'friday': 'пятница-развратница',
            'saturday': 'суббота-поебота',
            'sunday': 'вск - вых'}

def index(request):
    # rez = list(calendar)
    # li_elem = ''
    # for i in rez:
    #     redirect_path = reverse('todo_week-name',args=(i,))
    #     li_elem += f'<h2><li><a href={i}>{i.title()}</a></li></h2>'
    # response = f'<ol>{li_elem}<ol>'
    # return HttpResponse(response)
    return render(request, 'week_days/greeting.html')



def choose_day_of_week(request, sign_week: str):
    if sign_week.lower() in calendar:
        return HttpResponse(f'<h2>{calendar[sign_week.lower()]}</h2>')
    return HttpResponse('<h2>Нет такого дня недели<h2>')


def choose_day_of_week_int(request, sign_week: int):
    if 0 < sign_week <= 7:
        calin = list(calendar)
        redirect_url = reverse('todo_week-name',args=(calin[sign_week-1],))
        return HttpResponseRedirect(redirect_url)
    return HttpResponse(f'<h2>Неверный номер дня - {sign_week}</h2>')


