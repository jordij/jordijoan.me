from wagtail.wagtailcore import blocks
from commonblocks.blocks import CommonImageBlock


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
    )

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'
        template = 'commonblocks/code.html'


class ImageGalleryBlock(blocks.StructBlock):
    """
    Images gallery block
    """
    title = blocks.CharBlock(required=False)
    images = blocks.ListBlock(CommonImageBlock())

    class Meta:
        icon = 'image'
        template = 'blocks/image_gallery.html'
