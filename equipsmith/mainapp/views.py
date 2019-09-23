from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("EQUIP SMITH BLANK PAGE")


def bstest(request):
	return render(request, 'bstest.html')
	