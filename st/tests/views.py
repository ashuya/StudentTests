from django.shortcuts import render

# Create your views here.

def index(request):
	context = {
		'title': 'Тестики',
	}
	return render(request, 'tests/index.html', context)
