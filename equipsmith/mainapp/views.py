from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from mainapp.models import Equipments

# Create your views here.
def index(request):
	# return HttpResponse("EQUIP SMITH BLANK PAGE")
	return redirect("bstest")


def bstest(request):
	equipments_list = Equipments.objects.all()
	return render(request, 'bstest.html')
	