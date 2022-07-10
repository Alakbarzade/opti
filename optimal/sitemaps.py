from wagtail.core.models import Page
from translation.utils import get_translated_sitemap_urls

class ExtendedPage(Page):
    class Meta:
        abstract = True

    def get_translated_sitemap_urls(page, request, default_data):

        domains = settings.TRANSLATED_DOMAINS
        host = request.get_host()
        domain = None
        lang = None

        for k, v in domains.items():
            if v == host:
                domain = k
                lang = k

        if domain and lang:

            # return empty array if this page isn't the current language
            if page.language.code != lang:
                return []

            # get default sitemap data for page, return if no data
            data = next(iter(default_data))
            if not data:
                return []

            # get self and siblings, add to data and return
            siblings = get_translatable_page_siblings(page.__class__, page, only_live=True, include_self=True)
            data['alternates'] = siblings

            return [data]

        # return an empty array if none of the above
        return []