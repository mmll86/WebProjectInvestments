from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import ShareholderRegister
import datetime


def index(request):
	shareholders = ShareholderRegister.objects.all()
	context = {'shareholders': shareholders}
	return render(request, 'investments_register/index.html', context)


def shareholder_detail(request, slug):
	detail = ShareholderRegister.objects.get(slug__iexact=slug)
	context = {'detail': detail}
	return render(request, 'investments_register/shareholder_detail.html', context)
