from django.shortcuts import render
from . import forms



# Create your views here.



def contact(request):
	form=forms.contact_form(request.POST or None)
	print(form.is_bound)
	if form.is_valid():
		form.save()
	return render (request, 'contact/contact.html', { 'form': form })
