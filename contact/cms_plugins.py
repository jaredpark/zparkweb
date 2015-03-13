from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from contact.forms import ContactForm


class CMSContactPlugin(CMSPluginBase):
	name = _("Contact Plugin")  # Name of the plugin
	render_template = "contact/contact_plugin.html"  # template to render the plugin with

	def render(self, context, instance, placeholder):
		request = context['request']
		context.update({
			'instance': instance,
			'placeholder': placeholder,
			'contact_form': ContactForm(),
			})
		return context

plugin_pool.register_plugin(CMSContactPlugin)  # register the plugin