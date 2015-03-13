from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class HomepageApphook(CMSApp):
    name = _("Homepage Apphook")
    urls = ["homepage.urls"]

apphook_pool.register(HomepageApphook)