# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import modelcluster.fields
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('taggit', '0001_initial'),
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
        ('wagtaildocs', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(default=b'')),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Post date')),
            ],
            options={
                'verbose_name': 'Homepage',
                'description': 'The top level homepage for your site',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MenuElement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_external', models.URLField(help_text=b'Set an external link if you want the link to point somewhere outside the CMS.', null=True, verbose_name=b'External link', blank=True)),
                ('link_email', models.EmailField(help_text=b'Set the recipient email address if you want the link to send an email.', max_length=75, null=True, blank=True)),
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
            bases=(models.Model,),
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
            bases=(models.Model,),
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
        migrations.CreateModel(
            name='PageCarouselItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('embed_url', models.URLField(verbose_name=b'Embed URL', blank=True)),
                ('caption', models.CharField(max_length=255, blank=True)),
                ('image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageRelatedLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('link_external', models.URLField(help_text=b'Set an external link if you want the link to point somewhere outside the CMS.', null=True, verbose_name=b'External link', blank=True)),
                ('link_email', models.EmailField(help_text=b'Set the recipient email address if you want the link to send an email.', max_length=75, null=True, blank=True)),
                ('link_phone', models.CharField(help_text=b'Set the number if you want the link to dial a phone number.', max_length=20, null=True, blank=True)),
                ('title', models.CharField(help_text=b'Link title', max_length=255)),
                ('link_document', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtaildocs.Document', help_text=b'Choose an existing document if you want the link to open a document.', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='jordijoan.mePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('intro', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name=b'Post date')),
                ('comments', models.BooleanField(default=True, help_text=b'Comments are enabled by default. Uncheck the box if you would like to disable them for this         page.', verbose_name=b'Comments ON/OFF')),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True)),
                ('tags', modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='core.PageTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Springload standard page',
                'description': 'Standard page for your Springload site',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='pagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(related_name='tagged_items', to='core.jordijoan.mePage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagetag',
            name='tag',
            field=models.ForeignKey(related_name='core_pagetag_items', to='taggit.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagerelatedlink',
            name='link_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Choose an existing page if you want the link to point somewhere inside the CMS.', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagerelatedlink',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='related_links', to='core.jordijoan.mePage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagecarouselitem',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='carousel_items', to='core.jordijoan.mePage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuelement',
            name='link_document',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtaildocs.Document', help_text=b'Choose an existing document if you want the link to open a document.', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuelement',
            name='link_page',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailcore.Page', help_text=b'Choose an existing page if you want the link to point somewhere inside the CMS.', null=True),
            preserve_default=True,
        ),
    ]
