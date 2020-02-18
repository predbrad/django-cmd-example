import os

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    files = os.popen('ls -l').read()
    template = loader.get_template('templates/response.html')
    context = {
        'files': files
    }
    return HttpResponse(template.render(context,request))

    