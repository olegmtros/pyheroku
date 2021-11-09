from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse


def index(request):
    # return TemplateResponse('request', 'mainapp/index.html', locals())
    return render('request', 'mainapp/index.html', locals())
