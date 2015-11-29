# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import commonblocks.fields
import modelcluster.fields
import wagtail.wagtailimages.blocks
import django.db.models.deletion
import commonblocks.blocks
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0008_image_created_at_index'),
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
        ('wagtaildocs', '0003_add_verbose_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.StructBlock([(b'size', wagtail.wagtailcore.blocks.ChoiceBlock(help_text='Heading Size', choices=[(b'', 'Choose your heading'), (b'h2', b'h2'), (b'h3', b'h3'), (b'h4', b'h4'), (b'h5', b'h5')])), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'content', commonblocks.blocks.SimpleRichTextBlock()), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=True)), (b'alternative_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'caption', commonblocks.blocks.SimpleRichTextBlock(required=False)), (b'attribution', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'license_url', wagtail.wagtailcore.blocks.URLBlock(required=False)), (b'license_name', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.StreamBlock([(b'internal_link', wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.PageChooserBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False))], label='Internal page')), (b'external_link', wagtail.wagtailcore.blocks.StructBlock([(b'link', wagtail.wagtailcore.blocks.URLBlock(required=True)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'target', wagtail.wagtailcore.blocks.ChoiceBlock(default=b'_self', help_text='Open link in', choices=[(b'', b'Open link in'), (b'_self', b'Same window'), (b'_blank', b'New window')]))], label='External Page'))])), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'quote', commonblocks.blocks.SimpleRichTextBlock(required=True)), (b'author', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'author_title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False))])), (b'video', wagtail.wagtailcore.blocks.StructBlock([(b'video', wagtail.wagtailembeds.blocks.EmbedBlock(help_text='Paste your video URL ie: https://www.youtube.com/watch?v=05GKqTZGRXU', required=True)), (b'caption', commonblocks.blocks.SimpleRichTextBlock(required=False))]))], null=True, blank=True)),
                ('intro', commonblocks.fields.SimpleRichTextField(help_text='An excerpt of the page', null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Post date')),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'Article page',
                'description': 'Article page for your site',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'verbose_name': 'Homepage',
                'description': 'The homepage for your site',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MenuElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_external', models.URLField(help_text=b'Set an external link if you want the link to point somewhere outside the CMS.', null=True, verbose_name=b'External link', blank=True)),
                ('link_email', models.EmailField(help_text=b'Set the recipient email address if you want the link to send an email.', max_length=254, null=True, blank=True)),
                ('link_phone', models.CharField(help_text=b'Set the number if you want the link to dial a phone number.', max_length=20, null=True, blank=True)),
                ('explicit_name', models.CharField(help_text=b'If you want a different name than the page title.', max_length=64, null=True, blank=True)),
                ('short_name', models.CharField(help_text=b'If you need a custom name for responsive devices.', max_length=32, null=True, blank=True)),
                ('css_class', models.CharField(help_text=b'Optional styling for the menu item', max_length=255, null=True, verbose_name=b'CSS Class', blank=True)),
                ('icon_class', models.CharField(help_text=b'In case you need an icon element <i> for the menu item', max_length=255, null=True, verbose_name=b'Icon Class', blank=True)),
            ],
            options={
                'verbose_name': 'Menu item',
                'description': 'Elements appearing in the main menu',
            },
        ),
        migrations.CreateModel(
            name='NavigationMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Navigation menu',
                'description': 'Navigation menu',
            },
        ),
        migrations.CreateModel(
            name='PageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(help_text=b'Set an external link if you want the link to point somewhere outside the CMS.', null=True, verbose_name=b'External link', blank=True)),
                ('link_email', models.EmailField(help_text=b'Set the recipient email address if you want the link to send an email.', max_length=254, null=True, blank=True)),
                ('link_phone', models.CharField(help_text=b'Set the number if you want the link to dial a phone number.', max_length=20, null=True, blank=True)),
                ('title', models.CharField(help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtaildocs.Document', help_text=b'Choose an existing document if you want the link to open a document.', null=True)),
                ('link_page', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Choose an existing page if you want the link to point somewhere inside the CMS.', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='related_links', to='core.BasePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='core.BasePage')),
                ('tag', models.ForeignKey(related_name='core_pagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationMenuMenuElement',
            fields=[
                ('menuelement_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.MenuElement')),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('parent', modelcluster.fields.ParentalKey(related_name='menu_items', to='core.NavigationMenu')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('core.menuelement', models.Model),
        ),
        migrations.AddField(
            model_name='menuelement',
            name='link_document',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtaildocs.Document', help_text=b'Choose an existing document if you want the link to open a document.', null=True),
        ),
        migrations.AddField(
            model_name='menuelement',
            name='link_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Choose an existing page if you want the link to point somewhere inside the CMS.', null=True),
        ),
        migrations.AddField(
            model_name='basepage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='core.PageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
