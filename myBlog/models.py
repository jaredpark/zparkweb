from django.db import models
from django.contrib.auth.models import User

from djangocms_text_ckeditor.fields import HTMLField
from cms.models.fields import PlaceholderField

from utilities import slug_it

class Post(models.Model):

	title = models.CharField(max_length = 100, unique = True)
	slug = models.CharField(max_length = 100, unique = True)
	content = PlaceholderField('Blog Post Content', null=True, blank=True)
	tease = HTMLField(null=True, blank=True)
	author = models.ForeignKey(User)
	created_on = models.DateTimeField(auto_now_add = False)
	main_image = models.ImageField(null=True, blank=True, upload_to = './images')
	image_alt = models.CharField(max_length = 100, null=True, blank=True)

	def __unicode__(self):
		return(self.title)

	@models.permalink
	def get_absolute_url(self):
		return('myBlog_view_post',
			(),
			{ 'slug': self.slug, })

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slug_it(self.title)
		super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	name = models.CharField(max_length = 40)
	email = models.EmailField(max_length = 80)
	website = models.URLField(max_length = 200, null = True, blank = True)
	content = models.TextField()
	post = models.ForeignKey(Post)
	created_on = models.DateTimeField(auto_now_add = True)

	def __unicode__(self):
		return(self.content)
