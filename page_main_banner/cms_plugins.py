from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import PageMainBanner


@plugin_pool.register_plugin
class PageMainBannerPlugin(CMSPluginBase):
    model = PageMainBanner
    module = _("Page Main Banner Plugin")
    # name of the plugin in the interface
    name = _("PageMainBanner")
    render_template = "page_main_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(PageMainBannerPlugin, self).render(
            context, instance, placeholder)
        return context
