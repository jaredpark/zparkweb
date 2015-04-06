from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class MyBlogApphook(CMSApp):
    name = _("Blog Apphook")
    urls = ["myBlog.urls"]

apphook_pool.register(MyBlogApphook)