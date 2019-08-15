from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('equipsmith_main/index.html')
    return HttpResponse(template.render(None, request))
    # renderショートカットメソッドを用いた、上文と同意義の命令文
    # return render(request, 'equipsmith_main/index.html')