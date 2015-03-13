from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _

from myQuotes.models import Quote

import random

class CMSQuotePlugin(CMSPluginBase):
    name = _("Quote Plugin")  # Name of the plugin
    render_template = "myQuotes/myQuotes_plugin.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        last = Quote.objects.count() - 1
        rand_index = random.randint(0,last)
        rand_quote = Quote.objects.all()[rand_index]
        request = context['request']
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'quote_text': rand_quote.quote_text,
            'quote_author': rand_quote.quote_author,
            })
        return context

plugin_pool.register_plugin(CMSQuotePlugin)  # register the plugin