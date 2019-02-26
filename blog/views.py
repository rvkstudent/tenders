# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import pandas as pd

# Create your views here.

def show(request):
    template = loader.get_template('index.html')


    df = pd.read_excel(u'C:\\GOSZAKUPKI\\PREVIOUS\\tender-22.02.xls')

    table_dict = df.to_dict()

    context = {"headers" : list(df.columns),
               "dataframe" : df.to_html

               }

    return HttpResponse(template.render(context, request))

def username(request, username):
    template = loader.get_template('index.html')
    context = {'username': username}
    return HttpResponse(template.render(context, request))

def section(request, title, section):

    return HttpResponse('Title = {0}, section = {1}. Тип title = {2}, тип section = {3}'.format(title, section, type(title), type(section)))