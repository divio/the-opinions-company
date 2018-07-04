from django.db import models
from cms.models import CMSPlugin
from polls.models import Poll


class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Poll)

    def __str__(self):
        return self.poll.question
