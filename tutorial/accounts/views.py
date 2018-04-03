from django.shortcuts import HttpResponse, render

def home(request):
	return render(request, 'accounts/login.html')