from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_polls.models import PollPlugin
from django.utils.translation import ugettext as _

class CMSPollPlugin(CMSPluginBase):
    model = PollPlugin  # Model where data about this plugin is saved
    module = _("Polls")
    name = _("Poll Plugin")  # Name of the plugin
    render_template = "djangocms_polls/poll_plugin.html"  # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSPollPlugin)  # register the plugin