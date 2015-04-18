from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^myProfiles\.models\.SeparatedValuesField"])

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from registration.signals import user_registered
from datetime import datetime

from cms.models.fields import PlaceholderField

class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value, connection, prepared=False):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([str(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class UserProfile(models.Model):
# class UserProfile(FacebookProfileModel):
	user = models.ForeignKey(User, unique=True)
	first_name = models.CharField(default='',blank=False, max_length=20)
	last_name = models.CharField(default='',blank=False, max_length=20)
	company = models.CharField(default='',blank=True, max_length=100)
	url = models.URLField(default='http://www.none.com', blank=True, max_length=100)
	address = models.CharField(default='',blank=True, max_length=100)
	city = models.CharField(default='',blank=True, max_length=20)
	zipcode = models.IntegerField(default=1,blank=True, max_length=5)
	phone = models.CharField(default='',blank=True, max_length=12)
	email = models.EmailField(default='',blank=True, max_length=60)
	total_balance = models.DecimalField(default=0.00,blank=True,max_digits=6,decimal_places=2)
	current_balance = models.DecimalField(default=0.00,blank=True,max_digits=6,decimal_places=2)
	balance_due_date = models.DateField(blank=True, null=True)
	public = models.BooleanField(default=False,blank=True)
	notes = models.TextField(default='',blank=True,max_length=400)

	# user_profile_placeholder = PlaceholderField('user_profile_placeholder')

	class Meta:
		verbose_name = _('user profile')
		verbose_name_plural = _('user profiles')
		
	def __unicode__(self):
		return(self.user.username)

	def __str__(self):
		return(self.user.username)	 	

	def attrs(self):
		out = []
		for field in self._meta.fields:
			out.extend([field.name, getattr(self, field.name)])
		return(out)

	def user_registered_callback(sender, user, request, **kwargs):
		profile = UserProfile(user = user)
		profile.first_name = request.POST["first_name"]
		profile.last_name = request.POST["last_name"]
		profile.email = request.POST["email"]
		profile.save()
		user.first_name = request.POST["first_name"]
		user.last_name = request.POST["last_name"]
		user.email = request.POST["email"]
		user.save()
 
	user_registered.connect(user_registered_callback)

class UserImages(models.Model):
	user = models.ForeignKey(UserProfile, unique=True, related_name='images')
	user_image = models.ImageField(upload_to = "images/uploads/", null = True, blank = True)

	class Meta:
		verbose_name = _('user image')
		verbose_name_plural = _('user images')

	def __unicode__(self):
		return(self.user.user.username)

	def __str__(self):
		return(self.user.user.username)	

class UserProject(models.Model):
	user = models.ForeignKey(UserProfile, related_name='project')
	description = models.CharField(default='Project', max_length = 400)
	progress_url = models.URLField(default='http://www.none.com')
	design_url = models.TextField(blank=True, null = True, max_length = 2000)

	class Meta:
		verbose_name = _('user project')
		verbose_name_plural = _('user projects')

	def __unicode__(self):
		return(self.user.user.username)

	def __str__(self):
		return(self.user.user.username)