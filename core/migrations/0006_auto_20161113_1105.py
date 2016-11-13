# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160131_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'size', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Heading Size', choices=[(b'', b'Choose your heading'), (b'h2', b'h2'), (b'h3', b'h3'), (b'h4', b'h4'), (b'h5', b'h5')])), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(editor=b'default')), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), (b'alternative_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False, editor=b'simple')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'license_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), (b'license_name', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.StreamBlock([(b'internal_link', wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False))], label=b'Internal page')), (b'external_link', wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'target', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'_self', help_text=b'Open link in', choices=[(b'', b'Open link in'), (b'_self', b'Same window'), (b'_blank', b'New window')]))], label=b'External Page'))])), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', wagtail.wagtailcore.blocks.RichTextBlock(required=False, editor=b'simple')), (b'author', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'author_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'video', wagtail.wagtailcore.blocks.StructBlock([(b'video', wagtail.wagtailembeds.blocks.EmbedBlock(help_text=b'Paste your video URL ie: https://www.youtube.com/watch?v=05GKqTZGRXU', required=True)), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False, editor=b'simple'))])), (b'code', wagtail.wagtailcore.blocks.StructBlock([(b'language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'python', b'Python'), (b'bash', b'Bash/Shell'), (b'html', b'HTML'), (b'css', b'CSS'), (b'scss', b'SCSS')])), (b'code', wagtail.wagtailcore.blocks.TextBlock())])), (b'gallery', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'images', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), (b'alternative_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock(required=False, editor=b'simple')), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'license_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), (b'license_name', wagtail.wagtailcore.blocks.CharBlock(required=False))])))]))], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='basepage',
            name='intro',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
    ]
