from django import forms
from django.forms import ModelForm
from myProfiles.models import UserProfile, UserProject
from django.contrib.auth.models import User
from registration.forms import RegistrationForm

class MyRegistrationForm(RegistrationForm):
	first_name = forms.CharField(label='Your First Name')
	last_name = forms.CharField(label='Your Last Name')
	zipcode = forms.CharField(label='Your Zip Code', required=True)

class MyProfileForm(ModelForm):
	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'phone', 'email', 'address', 'city', 'zipcode')

class SubmitUrlForm(forms.Form):
	url = forms.URLField(label='Submit the URL of a new design idea', max_length=80)