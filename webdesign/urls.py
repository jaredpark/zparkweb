from django.conf.urls import patterns, include, url
from django.contrib import admin
from homepage import views

from myProfiles.forms import MyRegistrationForm, MyProfileForm
from registration.backends.default.views import RegistrationView

admin.autodiscover()

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return('/accounts/login/')

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # url(r'^$', include('homepage.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^contact/', include('contact.urls')),
	# url(r'^my_account/', include('user_interface.urls')),
    url(r'accounts/register/$', RegistrationView.as_view(form_class = MyRegistrationForm), name = 'registration_register'),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profiles/', include('myProfiles.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
