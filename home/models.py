from django.db import models

from wagtail.contrib.sitemaps.views import sitemap
from wagtail.models import Page, TranslatableMixin , PageBase
from wagtail.admin.panels import FieldPanel
from wagtailmetadata.models import MetadataPageMixin
from wagtailmetadata.models import MetadataMixin
from wagtailmetadata.models import WagtailImageMetadataMixin
from django.conf.urls.i18n import i18n_patterns



class HomePage(MetadataPageMixin, Page):
    object_type = "website"
    schemaorg_type = "website"

    template = "home/home_page.html"





    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_title2 = models.CharField(max_length=100, blank=False, null=True)
    banner_title3 = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_title2"),
        FieldPanel("banner_title3"),


    ]






