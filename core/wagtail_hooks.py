from wagtail.wagtailcore import hooks
from django.utils.html import format_html_join
from django.conf import settings
from wagtail.wagtailcore.whitelist import attribute_rule, check_url, allow_without_attributes


@hooks.register('insert_editor_css')
def editor_css():
    """
    Add extra CSS files to the admin
    """
    css_files = [
        'wagtailadmin/css/vendor/font-awesome-4.2.0/css/font-awesome.min.css',
        'wagtailadmin/css/admin.css',
    ]

    css_includes = format_html_join(
        '\n', '<link rel="stylesheet" href="{0}{1}">', ((settings.STATIC_URL, filename) for filename in css_files))
    return css_includes


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    """
    Whitelist custom elements to the hallo.js editor
    """
    return {
        'blockquote': allow_without_attributes,
        'cite': allow_without_attributes,
        'a': attribute_rule({'href': check_url, 'class': True}),
        'h2': attribute_rule({'id': True}),
        'h3': attribute_rule({'id': True}),
        'h4': attribute_rule({'id': True}),
        'h5': attribute_rule({'id': True}),
    }
