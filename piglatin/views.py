from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def translate(request):
	text_from_form = request.GET['original_text'].lower()

	translation = ''
	for word in text_from_form.split():
		if word[0] in ['a', 'i', 'o', 'e', 'u']:
			translation += word
			translation += 'yay '
		else:
			translation += word[1:]
			translation += word[0]
			translation += 'ay '


	return HttpResponse("You are on translate page " + translation )