from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from .models import ImageGallery,ImageGalleryInlineAdmin


@plugin_pool.register_plugin
class ImageGalleryPlugin(CMSPluginBase):
    inlines = (ImageGalleryInlineAdmin,)
    model = ImageGallery
    module = _("Image Gallery Plugin")
    name = _("ImageGallery")  # name of the plugin in the interface
    render_template = "image_gallery_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ImageGalleryPlugin, self).render(
            context, instance, placeholder)
            
        image_list = instance.image_items.all().order_by('id')
        context.update({'image_list': image_list})
        return context
