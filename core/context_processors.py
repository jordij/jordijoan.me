from django.conf import settings

import wagtail
from wagtail.wagtailcore.models import Site


def google_analytics(request):
    """
    Use the variables returned in this function to
    render your Google Analytics tracking code template.
    """
    ga_key = getattr(settings, 'GOOGLE_ANALYTICS_KEY', False)
    ga_tag = getattr(settings, 'GOOGLE_TAG_MANAGER', False)

    if ga_key:
        return {
            'GOOGLE_ANALYTICS_KEY': ga_key,
            'GOOGLE_TAG_MANAGER': ga_tag,
        }
    return {}


def baseurl(request):
    """
    Return a BASE_URL template context for the current request.
    """
    if request.is_secure():
        scheme = 'https://'
    else:
        scheme = 'http://'

    return {'BASE_URL': scheme + request.get_host(), }


def wagtail_version(request):
    return {'wagtail_version': wagtail.VERSION}


def root_site(request):
    site = Site.find_for_request(request)
    real_site_name = None
    if site:
        real_site_name = site.site_name if site.site_name else site.hostname
    return {'root_site': real_site_name if real_site_name else settings.WAGTAIL_SITE_NAME}