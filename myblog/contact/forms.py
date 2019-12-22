from django import forms
from .models import contact




class contact_form (forms.ModelForm):
	class Meta:
		model = contact
		fields =['name','email', 'messege']
		
		widgets = {
              
			'name'   : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Name'}),
            'email'  : forms.TextInput(attrs={'class': 'form-control',  'placeholder' : 'Email'}),
        	'messege': forms.Textarea(attrs= {'class': 'form-control',  'placeholder' : 'Your Messege'}),
        }

		



		
					 

	

