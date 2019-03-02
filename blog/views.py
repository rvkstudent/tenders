# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd
import urllib.parse
import re
from .models import TendersTsc

# Create your views here.

def show(request):

    template = loader.get_template('index.html')



    context = { "headers": ['Номер','Организация','Описание', 'Цена', 'Когда найден', 'Конкурс', 'Статус', 'Дата размещения', 'Найдено по фразе', 'Ссылка','Менеджер', 'Комментарий'],
                'dataframe_rows': list(TendersTsc.objects.all()),

               }

    return HttpResponse(template.render(context, request))

def username(request, username):
    template = loader.get_template('index.html')
    context = {'username': username}
    return HttpResponse(template.render(context, request))

def section(request, title, section):

    return HttpResponse('Title = {0}, section = {1}. Тип title = {2}, тип section = {3}'.format(title, section, type(title), type(section)))

def postdata(request):

    result = re.findall(r'row-\d+=\D*&', urllib.parse.unquote(str(request.body)))

    res = ''

    for elem in result:
        res = "Процедура {}, значение {} ".format(elem.split('=')[0].replace('row-', ''),
                                                  elem.split('=')[1].replace('&', ''))

    return HttpResponse(res)
