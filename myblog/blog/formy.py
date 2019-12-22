from django.shortcuts import render
from django.contrib.auth import login , authentication
from account.forms import RegistrationForm 
def registration(request):
	