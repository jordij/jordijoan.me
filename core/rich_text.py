import json

from django.conf import settings

from wagtail.wagtailadmin.rich_text import HalloRichTextArea


class RichTextArea(HalloRichTextArea):
    """
        Class used to instance RichText editors based on settings.WAGTAIL_EDITOR_OPTIONS['default'] configuration
    """
    def render_js_init(self, id_, name, value):
        editor_options = settings.WAGTAIL_EDITOR_OPTIONS['default']

        return "makeHalloRichTextEditable({0}, {1});".format(
            json.dumps(id_),
            json.dumps(editor_options)
        )


class SimpleRichTextArea(HalloRichTextArea):
    """
        Class used to instance RichText editors based on settings.WAGTAIL_EDITOR_OPTIONS['simple'] configuration
    """
    def render_js_init(self, id_, name, value):
        editor_options = settings.WAGTAIL_EDITOR_OPTIONS['simple']

        return "makeHalloRichTextEditable({0}, {1});".format(
            json.dumps(id_),
            json.dumps(editor_options)
        )
