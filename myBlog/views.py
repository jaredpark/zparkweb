from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext

from myBlog.models import Post, Comment
from myBlog.forms import CommentForm

def view_post(request, slug):
	post = get_object_or_404(Post, slug = slug)
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid:
			comment = comment_form.save(commit=False)
			comment.post = post
			comment.save()
			return(redirect(request.path))
	else:
		comment_form = CommentForm()
		# comment_form.initial['name'] = 'Your name'
	return(render_to_response('myBlog/blog_post.html', 
								{'post': post, 'comment_form': comment_form, }, 
								context_instance = RequestContext(request) ) )

def blog_home(request):
	all_blogs = Post.objects.all()
	n_blogs = len(all_blogs)
	max_display = min(n_blogs, 5)
	blog_list = all_blogs.order_by('-id')[0:max_display]
	return(render_to_response('myBlog/blog_home.html',
								{'blog_list': blog_list, }, 
								context_instance = RequestContext(request) ) )


