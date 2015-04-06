from context_processors import site_settings_processor
from django.core.mail import send_mail, EmailMessage
import datetime
import os
import re

from contact.forms import ContactForm, CouponForm

def admin_name():
    return site_settings_processor(None)['admin_name']

def project_name():
    return site_settings_processor(None)['project_name']

def slug_it(string_to_slug):
	slug = re.sub(' ', '-', string_to_slug)
	return(slug)

is_production = os.environ.get('IS_PRODUCTION')

def CouponFormProcessor(request, context_dictionary):
	if request.method == 'POST':
		if 'specials' in request.POST:
			# create a form instance and populate it with data from the request:
			coupon_form = CouponForm(request.POST)
			# check whether it's valid:
			if coupon_form.is_valid():
				first_name = coupon_form.cleaned_data['first_name']
				last_name = coupon_form.cleaned_data['last_name']
				zipcode = coupon_form.cleaned_data['zipcode']
				phone = coupon_form.cleaned_data['phone']
				website_visitor = coupon_form.cleaned_data['email']
				contact_permission = coupon_form.cleaned_data['permission']
				company_email = site_settings_processor(request)['site_email']
				header = 'First name,' + 'last name,' + 'Zip Code,' + 'Main Phone,' + 'Email,' + 'CF[Marketing_permission],'
				form_data = first_name + "," + last_name + "," + str(zipcode) + "," + phone + "," + website_visitor + "," + str(contact_permission)
				fullemail = header + form_data
				time_stamp = str(datetime.datetime.now())
				to_company_email_object = EmailMessage(subject = 'website coupon inquiry', body = form_data, from_email = website_visitor, to = [company_email,], attachments = [(time_stamp+'.txt',fullemail,),])
				to_company_email_object.send()
				to_visitor_email_object = EmailMessage(subject = 'Test Coupon Email Subject', body = 'Test Coupon Email Body', from_email = company_email, to = [website_visitor,])
				if is_production:
					prefix = project_name() + '/'
				else:
					prefix = ''
				to_visitor_email_object.attach_file(prefix + 'static/documents/coupon_firstdraft.pdf')
				to_visitor_email_object.send()
				context_dictionary['first_name'] = first_name
			else:
				context_dictionary['form_errors'], context_dictionary['coupon_form'] = True, coupon_form
		else:
			pass
	else:
		coupon_form = CouponForm()
		context_dictionary['coupon_form'] = coupon_form

def ContactFormProcessor(request, context_dictionary):
	context_dictionary['name_placeholder'] = 'Your name'
	context_dictionary['email_placeholder'] = 'Your email'
	context_dictionary['phone_placeholder'] = 'XXX-XXX-XXXX'
	context_dictionary['message_placeholder'] = 'How can we help?'
	context_dictionary['name_value']=context_dictionary['email_value']=context_dictionary['phone_value']=context_dictionary['message_value'] = ''
	context_dictionary['error_fields'] = []
	if request.method == 'POST':
		if 'contact' in request.POST:
			# create a form instance and populate it with data from the request:
			contact_form = ContactForm(request.POST)
			# check whether it's valid:
			if contact_form.is_valid():
				name = contact_form.cleaned_data['name']
				phone = contact_form.cleaned_data['phone']
				sender = contact_form.cleaned_data['email']
				message_body = contact_form.cleaned_data['message']
				recipients = [site_settings_processor(request)['site_email'],]
				# from_email = site_settings_processor(request)['site_email']
				from_email = sender
				header = 'CF[Name],' + 'Main Phone,' + 'Email,' + 'CF[Message]\n'
				fullemail = header + name + "," + phone + "," + sender + "," + message_body
				time_stamp = str(datetime.datetime.now())
				email_object = EmailMessage(subject = 'URGENT website contact form email', body = message_body, from_email = from_email, to = recipients, attachments = [(time_stamp+'.txt',fullemail,),])
				email_object.send()
				# send_mail(subject = subject, message = fullemail, from_email = from_email, recipient_list = recipients)
				context_dictionary['name'] = name.split(' ')[0]
			else:
				context_dictionary['contact_form'] = contact_form
				for field in contact_form:
					context_dictionary[field.name + '_value'] = contact_form[field.name].value
				for field in contact_form.errors:
					error_message = contact_form.errors[field][0]
					context_dictionary[field + "_placeholder"] = error_message
					context_dictionary['error_fields'].append(field)
		else:
			pass
	else:
		contact_form = ContactForm()
		context_dictionary['contact_form'] = contact_form

from django.db.models import ImageField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

class ContentTypeRestrictedImageField(ImageField):
	"""
	Same as ImageField, but you can specify:
	* content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
	* max_upload_size - a number indicating the maximum file size allowed for upload.
	2.5MB - 2621440
	5MB - 5242880
	10MB - 10485760
	20MB - 20971520
	50MB - 5242880
	100MB 104857600
	250MB - 214958080
	500MB - 429916160
	"""
	def __init__(self, *args, **kwargs):
		# self.content_types = kwargs.pop("content_types")
		self.max_upload_size = kwargs.pop("max_upload_size")
		super(ContentTypeRestrictedImageField, self).__init__(*args, **kwargs)
	def clean(self, *args, **kwargs):        
		data = super(ContentTypeRestrictedImageField, self).clean(*args, **kwargs)
		file = data.file
		try:
			# content_type = file.content_type
			# if content_type in self.content_types:
				if file._size > self.max_upload_size:
					raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
			# else:
				# raise forms.ValidationError(_('Filetype not supported.'))
		except AttributeError:
			pass        

		return data

from south.modelsinspector import add_introspection_rules
add_introspection_rules([
	(
		[ContentTypeRestrictedImageField], # Class(es) these apply to
		[],         # Positional arguments (not used)
		{           # Keyword argument
			"max_upload_size": ["max_upload_size", {}],
		},
	),
	], ["^utilities\.ContentTypeRestrictedImageField"])
