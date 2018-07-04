from django import template
from django.core.exceptions import ObjectDoesNotExist

from core.snippets import NavigationMenu

register = template.Library()


@register.filter
def content_type(model):
    """
    Return the model name/"content type" as a string e.g BlogPage.
    Can be used with "slugify" to create CSS-friendly classnames
    Usage: {% raw %}{{ self|content_type|slugify }} {% endraw %}
    """
    return model.__class__.__name__


@register.inclusion_tag('core/includes/footer.html', takes_context=True)
def footer(context):
    """
    Retrieves the MenuElement(s) under the NavigationMenu with menu_name as "footer"
    """
    try:
        items = NavigationMenu.objects.get(menu_name='footer').items
    except ObjectDoesNotExist:
        return None

    result = {'items': items}
    result['request'] = context['request'] if 'request' in context else None
    return result


@register.inclusion_tag('core/includes/menu.html', takes_context=True)
def main_menu(context):
    """
    Retrieves the MenuElement(s) under the NavigationMenu with menu_name as "main"
    """
    try:
        items = NavigationMenu.objects.get(menu_name='main').items
    except ObjectDoesNotExist:
        return None
    result = {'items': items}
    result['request'] = context['request'] if 'request' in context else None
    result['self'] = context['self'].specific if 'self' in context else None
    result['category'] = context['category'] if 'category' in context else None
    return result


class SetVarNode(template.Node):

    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

    def render(self, context):
        try:
            value = template.Variable(self.var_value).resolve(context)
        except template.VariableDoesNotExist:
            value = ""
        context[self.var_name] = value
        return u""


@register.tag(name='set')
def set_var(parser, token):
    """
    Usage: {% set var_name  = var_value %}
    """
    parts = token.split_contents()
    if len(parts) < 4:
        raise template.TemplateSyntaxError("'set' tag must be of the form:  {% set var_name  = var_value %}")
    return SetVarNode(parts[1], parts[3])
