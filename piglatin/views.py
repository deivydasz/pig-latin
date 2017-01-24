from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def translate(request):
	text_from_form = request.GET['original_text']
	return HttpResponse("You are on translate page " + text_from_form )