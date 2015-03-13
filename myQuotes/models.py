from django.db import models
from django.utils.translation import ugettext_lazy as _

class Quote(models.Model):
	quote_text = models.TextField(_(u'Quote Text'))
	quote_author = models.CharField(_(u'Quote Author'), max_length = 255)
	quote_date = models.DateField(_(u'Quote Date'), auto_now_add = True)

	def __unicode__(self):
		return(self.quote_author)