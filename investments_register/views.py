from django.shortcuts import render

# Create your views here.
def index(request):
	text = 'Investments'
	context = {'text': text}
	return render(request, 'investments_register/index.html', context)
