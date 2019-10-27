from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.
def index(request):
	# return HttpResponse("EQUIP SMITH BLANK PAGE")
	return redirect("bstest")


def bstest(request):
	return render(request, 'bstest.html')
	