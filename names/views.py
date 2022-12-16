from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from dataclasses import dataclass
# Create your views here.
signs = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}
types = {'fire': ['aries', 'leo', 'sagittarius'],
         'earth': ['taurus', 'virgo', 'capricorn'],
         'air': ['gemini', 'libra', 'aquarius'],
         'water': ['cancer', 'scorpio', 'pisces']
         }

days = {1: ['capricorn', 'aquarius', 20, 31],
        2: ['aquarius', 'pisces', 19, 28],
        3: ['pisces', 'aries', 20, 31],
        4: ['aries', 'taurus', 20, 30],
        5: ['taurus', 'gemini', 21, 31],
        6: ['gemini', 'cancer', 21, 30],
        7: ['cancer', 'leo', 22, 31],
        8: ['leo', 'virgo', 21, 31],
        9: ['virgo', 'libra', 23, 30],
        10: ['libra', 'scorpio', 23, 31],
        11: ['scorpio', 'sagittarius', 22, 30],
        12: ['sagittarius', 'capricorn', 20, 31]
        }


def index(request):
    elem_zodiac = list(signs)
    # li_elem += f"<h2><li> <a href='{i}'>{i.title()}</a> </li></h2>"
    zodiacss = {'elem_zodiac':elem_zodiac,
                'signs' : {}
                }
    return render(request,'names/title.html',context=zodiacss)


def types_of_zodiack(request):
    typp = list(types)
    li_elem = ''
    for i in typp:
        redirect_path = reverse('type-name', args=(i,))
        li_elem += f'<h2><li><a href=type/{i}>{i.title()}</a> </li></h2>'
    response = f'<ol>{li_elem}</ol>'
    return HttpResponse(response)


def group_of_zodiack(request, zodiac: str):
    typp = list(types.values())
    li_elem = ''
    if zodiac == 'fire':
        for i in typp[0]:
            redirect_path = reverse('type-name', args=(i,))
            li_elem += f'<h2><li><a href=/horoscope/{i}>{i.title()}</a> </li></h2>'
        responce = f'<ol>{li_elem}</ol>'
        return HttpResponse(responce)
    if zodiac == 'earth':
        for i in typp[1]:
            redirect_path = reverse('type-name', args=(i,))
            li_elem += f'<h2><li><a href=/horoscope/{i}>{i.title()}</a> </li></h2>'
        responce = f'<ol>{li_elem}</ol>'
        return HttpResponse(responce)
    if zodiac == 'air':
        for i in typp[2]:
            redirect_path = reverse('type-name', args=(i,))
            li_elem += f'<h2><li><a href=/horoscope/{i}>{i.title()}</a> </li></h2>'
        responce = f'<ol>{li_elem}</ol>'
        return HttpResponse(responce)
    if zodiac == 'water':
        for i in typp[3]:
            redirect_path = reverse('type-name', args=(i,))
            li_elem += f'<h2><li><a href=/horoscope/{i}>{i.title()}</a> </li></h2>'
        responce = f'<ol>{li_elem}</ol>'
        return HttpResponse(responce)


def get_info_about_sign_zodiace(request, sign_zodiac: str):
    description = signs.get(sign_zodiac)
    data = {'description_zodiac': description,
            'name_of_zodiac': sign_zodiac,
            'signs_zodiac_ru' : signs,
            }
    return render(request, 'names/info_zodiac.html', context=data)


def get_info_about_sign_zodiace_int(request, sign_zodiac: int):
    if sign_zodiac > len(signs):
        return HttpResponse(f'Erorr. We have not what zodiac sign {sign_zodiac}')
    sign_lst = list(signs)
    s = sign_lst[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(s,))
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month: int, day: int):
    if month > 12:
        return HttpResponse(f'<h2>Месяц - {month}, День - {day} >>>Не найдены<br><br>Введите корректные данные</h2>')
    else:
        if day <= days[month][2]:
            s = days[month][0]
            redirect_url = reverse('horoscope-name', args=(s,))
            return HttpResponseRedirect(redirect_url)
        if days[month][2] <= day <= days[month][3]:
            s = days[month][1]
            redirect_url = reverse('horoscope-name', args=(s,))
            return HttpResponseRedirect(redirect_url)

        return HttpResponse(f'<h2>Месяц - {month}, День - {day} >>>Не найдены,<br><br>Введите корректные данные</h2>')




# def task_from_Artem(request,randoming):
#     datas = {'year_born': 1999,
#              'city_born' : 'Kishinev',
#              'movie_name': 'Matrix',
#              }
#     return render(request,'names/tasks.html',context=datas)
#
#
# def get_guinness_world_records(request,randoming):
#     context = {
#         'power_man': 'Narve Laeret',
#         'bar_name': 'Bob’s BBQ & Grill',
#         'count_needle': 1790,
#     }
#     return render(request, 'names/guinnessworldrecords.html', context=context)