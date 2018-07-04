from django.core.urlresolvers import reverse

from cms.utils.urlutils import admin_reverse
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar.items import LinkItem, SideframeItem, Button, BaseItem, Break, Menu, ButtonList
from cms.constants import RIGHT, LEFT, REFRESH_PAGE, URL_CHANGE

from polls.models import Poll


class PollToolbar(CMSToolbar):

    supported_apps=['polls']

    def populate(self):

        if not self.is_current_app:
            return

        menu = self.toolbar.get_or_create_menu('polls_cms_integration-polls', 'Polls')

        menu.add_sideframe_item(
            name='Poll list',                              # name of the new menu item
            url=admin_reverse('polls_poll_changelist'),    # the URL it should open with
            )


toolbar_pool.register(PollToolbar)
