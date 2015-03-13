from django import forms

class ContactForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	name = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'name_field',}))
	email = forms.EmailField(label='', required=True, widget=forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'email_field',}),
		error_messages={'required': 'This field is required - we promise to never sell your information!', 'invalid': 'Please enter numbers only'})
	phone = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Your phone number', 'class': 'phone_field',}),
		error_messages={'required': 'This field is required - we promise to never sell your information!', 'invalid': 'Please enter numbers only'})
	message = forms.CharField(label='', max_length=400, widget=forms.TextInput(attrs={'placeholder': 'How can we help?', 'class': 'message_field',}))

class CouponForm(forms.Form):
	error_css_class = 'error'
	required_css_class = 'required'
	first_name = forms.CharField(label='First Name', required=True)
	last_name = forms.CharField(label='Last Name', required=True)
	zipcode = forms.IntegerField(label='Zip Code', required=True)
	email = forms.EmailField(label='Email Address', required=True)
	phone = forms.CharField(label='Phone Number', required=True)
	permission = forms.BooleanField(label="Do you want to know the 5 things your bug guy hasn't told you?", required=False, initial=True)
