# Amend these to the domains your translated site uses
TRANSLATED_DOMAINS = {
    'en': 'localhost/en/',
    'ru': 'localhost',
    'az': 'localhost/az/',
}

def get_translatable_page_siblings(instance, only_live=True, include_self=False):

    translations = instance.get_translations(inclusive=include_self)

    if only_live:
        translations = translations.live()

    return translations

def get_translated_sitemap_urls(page, request, default_data):

    domains = TRANSLATED_DOMAINS
    host = request.get_host()
    domain = None
    lang = None

    for k, v in domains.items():
        if v == host:
            domain = v
            lang = k

    if domain and lang:

        # return empty array if this page isn't the current language
        if page.locale.language_code != lang:
            return []

        # get default sitemap data for page, return if no data
        data = next(iter(default_data))
        if not data:
            return []

        # get self and siblings, add to data and return
        siblings = get_translatable_page_siblings(page, only_live=True, include_self=True).select_related('locale')
        data['alternates'] = siblings

        return [data]

    # return an empty array if none of the above
    return []