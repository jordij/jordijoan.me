# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151129_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=155)),
                ('slug', models.SlugField(unique=True, max_length=80)),
                ('description', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.RemoveField(
            model_name='menuelement',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='menuelement',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='navigationmenumenuelement',
            name='menuelement_ptr',
        ),
        migrations.RemoveField(
            model_name='navigationmenumenuelement',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='pagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='pagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='pagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='MenuElement',
        ),
        migrations.DeleteModel(
            name='NavigationMenu',
        ),
        migrations.DeleteModel(
            name='NavigationMenuMenuElement',
        ),
        migrations.DeleteModel(
            name='PageRelatedLink',
        ),
        migrations.AddField(
            model_name='basepage',
            name='category',
            field=models.ForeignKey(related_name='pages', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.Category', null=True),
        ),
    ]
