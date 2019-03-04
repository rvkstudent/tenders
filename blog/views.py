# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd
import urllib.parse
import re
from .models import TendersTsc
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show(request):

    template = loader.get_template('index.html')



    context = { "headers": ['Номер','Организация','Описание', 'Цена', 'Когда найден', 'Конкурс', 'Статус', 'Дата размещения', 'Найдено по фразе', 'Ссылка','Регион', 'Комментарий'],
                'dataframe_rows': list(TendersTsc.objects.all()),

               }

    return HttpResponse(template.render(context, request))

def username(request, username):
    template = loader.get_template('index.html')
    context = {'username': username}
    return HttpResponse(template.render(context, request))

def section(request, title, section):

    return HttpResponse('Title = {0}, section = {1}. Тип title = {2}, тип section = {3}'.format(title, section, type(title), type(section)))

@csrf_exempt
def postdata(request):

    result_body = urllib.parse.unquote(str(request.body))

    result = result_body.replace('b\"', '').split('&')

    res = ''

    if len(result)>0:

        for elem in result:

            id = elem.split('=')[0].replace('row-', '')

            if len(id) > 0:

                try:

                    item = TendersTsc.objects.get(tender_id=id)

                    value = elem.split('=')[1].replace('&', '')

                    item.comment = value

                    item.save()

                    res = res + 'Записан элемент {} значение {}; '.format(id, value)

                except Exception as e:
                    pass

    return HttpResponse("Данные обновлены")
