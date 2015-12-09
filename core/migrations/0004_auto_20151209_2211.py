# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
        ('wagtaildocs', '0003_add_verbose_names'),
        ('core', '0003_auto_20151209_2202'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, max_length=80, blank=True),
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
    ]
