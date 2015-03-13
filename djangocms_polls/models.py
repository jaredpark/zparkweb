from cms.models import CMSPlugin
from django.db import models
from polls.models import Poll

class PollPlugin(CMSPlugin):
    poll = models.ForeignKey(Poll)

    def __unicode__(self):
      return self.poll.question