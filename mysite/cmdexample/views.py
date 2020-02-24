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

    
def tail_log(request):
    #TODO put some max size here or keep track of the line you're reading from or something?
    
    log_output = ""
    with open(os.path.join(os.getcwd(), 'my_log.txt'),'rU') as f:
        for line in f:
            log_output += line

    template = loader.get_template('templates/log.html')
    context = {
        'log_output': log_output
    }
    return HttpResponse(template.render(context,request))

    