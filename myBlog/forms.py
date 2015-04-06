from django import forms
from django.forms import ModelForm
from myBlog.models import Comment

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'website', 'content')

