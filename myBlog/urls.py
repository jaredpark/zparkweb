from django.conf.urls import patterns, url

# from myBlog.forms import CommentForm
from myBlog import views


urlpatterns = patterns('',
  # url(r'^edit', 
  #   views.edit_profile, 
  #   {'form_class': MyProfileForm},
  #   name='profiles_edit_profile'),
  url(r'^(?P<slug>[-\w]+)$',
    views.view_post,
    name='myBlog_view_post'),
  url(r'^$',
  	views.blog_home, 
  	name = 'blog_home'),
)
