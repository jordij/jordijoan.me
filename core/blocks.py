from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from django.conf import settings
from django.utils.safestring import mark_safe

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

DEFAULT_COMMONBLOCKS_HEADING = (
    ('h2', 'h2'),
    ('h3', 'h3'),
    ('h4', 'h4'),
    ('h5', 'h5'),
)

TARGETS = (
    ('', 'Open link in'),
    ('_self', 'Same window'),
    ('_blank', 'New window'),
)

HEADINGS = (('', 'Choose your heading'), ) + getattr(settings, 'COMMONBLOCKS_HEADINGS', DEFAULT_COMMONBLOCKS_HEADING)


class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block
    """
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
        ('json', 'JSON'),
    )

    STYLE_CHOICES = (
        ('syntax', 'default'),
        ('emacs', 'emacs'),
        ('monokai', 'monokai'),
        ('vim', 'vim'),
        ('xcode', 'xcode'),
    )

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    style = blocks.ChoiceBlock(choices=STYLE_CHOICES, default='syntax')
    code = blocks.TextBlock()

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']
        lexer = get_lexer_by_name(lang)
        css_classes = ['code', value['style']]

        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass=' '.join(css_classes),
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))

    class Meta:
        icon = 'code'
        template = 'blocks/code.html'


class CommonImageBlock(blocks.StructBlock):
    """
    Block for single images with all necessary attributes such as alternative title, caption and so on.
    """
    image = ImageChooserBlock(required=True)
    alternative_title = blocks.CharBlock(required=False)
    caption = blocks.RichTextBlock(editor='simple', required=False)
    attribution = blocks.CharBlock(required=False)
    license_url = blocks.URLBlock(required=False)
    license_name = blocks.CharBlock(required=False)

    @property
    def get_title(self):
        if self.alternative_title:
            return self.alternative_title
        else:
            self.image.title

    class Meta:
        icon = 'image'
        template = 'blocks/image.html'


class ImageGalleryBlock(blocks.StructBlock):
    """
    Images gallery block
    """
    title = blocks.CharBlock(required=False)
    images = blocks.ListBlock(CommonImageBlock())

    class Meta:
        icon = 'image'
        template = 'blocks/image_gallery.html'


class CommonQuoteBlock(blocks.StructBlock):
    """
    Block for rich text quotes
    """
    quote = blocks.RichTextBlock(editor='simple', required=False)
    author = blocks.CharBlock(required=False)
    author_title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'openquote'
        template = 'blocks/quote.html'


class CommonHeadingBlock(blocks.StructBlock):
    """
    Heading Block
    """
    size = blocks.ChoiceBlock(required=True, choices=HEADINGS, help_text='Heading Size')
    title = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=False)

    class Meta:
        icon = 'title'
        template = 'blocks/heading.html'


class CommonVideoBlock(blocks.StructBlock):
    """
    Video block
    """
    video = EmbedBlock(
        required=True,
        help_text='Paste your video URL ie: https://www.youtube.com/watch?v=05GKqTZGRXU'
    )
    caption = blocks.RichTextBlock(editor='simple', required=False)

    class Meta:
        icon = 'media'
        template = 'blocks/video.html'


class CommonInternalLink(blocks.StructBlock):
    """
    Single Internal link block
    """
    link = blocks.PageChooserBlock(required=True)
    title = blocks.CharBlock(required=False)

    @property
    def get_title(self):
        if self.title:
            return self.title
        else:
            self.link.title

    class Meta:
        template = 'blocks/internal_link.html'
        icon = 'link'


class CommonExternalLink(blocks.StructBlock):
    """
    Single External Tile Block
    """
    link = blocks.URLBlock(required=True)
    title = blocks.CharBlock(required=True)
    target = blocks.ChoiceBlock(
        required=True,
        choices=TARGETS,
        default='_self',
        help_text='Open link in'
    )

    class Meta:
        template = 'blocks/external_link.html'
        icon = 'site'


class CommonLinksBlock(blocks.StreamBlock):
    """
    A collection of Link Blocks, Orderable
    """
    internal_link = CommonInternalLink(label='Internal page')
    external_link = CommonExternalLink(label='External Page')

    class Meta:
        template = 'blocks/links.html'
        icon = 'link'
