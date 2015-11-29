from datetime import date

import django.db.models.options as options
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase
from bs4 import BeautifulSoup
from commonblocks.blocks import *
from commonblocks.fields import SimpleRichTextField

from core.snippets import LinkFields
from core.blocks import CodeBlock

options.DEFAULT_NAMES = options.DEFAULT_NAMES + ('description',)


class RelatedLink(LinkFields):
    """
    Title + link class inheriting from LinkFields
    """
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class HomePage(Page):
    """
    HomePage class, inheriting from wagtailcore.Page straight away
    """
    subpage_types = ['core.BasePage']
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    search_fields = ()

    def get_context(self, request):
        # Get pages
        pages = BasePage.objects.child_of(self).live()

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            pages = pages.filter(tags__name=tag)

        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(pages, 6)  # Show 6 pages per page
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        # Update template context
        context = super(HomePage, self).get_context(request)
        context['pages'] = pages
        return context

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "SEO and metadata fields"),
        ImageChooserPanel('feed_image'),
    ]

    class Meta:
        description = "The homepage for your site"
        verbose_name = "Home Page"


class PageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('core.BasePage', related_name='related_links')


class PageTag(TaggedItemBase):
    content_object = ParentalKey('core.BasePage', related_name='tagged_items')


class BasePage(Page):
    """
    Our main custom Page class. All content pages should inherit from this one.
    """
    body = StreamField(
        [
            ('heading', CommonHeadingBlock()),
            ('content', SimpleRichTextBlock()),
            ('image', CommonImageBlock()),
            ('links', CommonLinksBlock()),
            ('quote', CommonQuoteBlock()),
            ('video', CommonVideoBlock()),
            ('code', CodeBlock()),
        ],
        null=True,
        blank=True,
    )
    intro = SimpleRichTextField(
        help_text=_('An excerpt of the page'),
        null=True,
        blank=True,
    )
    date = models.DateField("Post date", default=date.today)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=PageTag, blank=True)
    search_fields = (
        index.SearchField('intro_text', boost=1),
        index.SearchField('body_text', boost=1),
        index.FilterField('date'),
    )

    @property
    def parent(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().last()

    @property
    def body_text(self):
        """
        Returns body field contents text. Useful for search purposes
        """
        return BeautifulSoup(self.body).get_text()

    @property
    def intro_text(self):
        """
        Returns intro field contents text. Useful for search purposes
        """
        return BeautifulSoup(self.intro).get_text()

    @property
    def body_excerpt(self):
        """
        Return body text replacing end of lines (. ? ! chars) with a blank space
        """
        return re.sub(r'([\.?!])([a-zA-Z])', r'\1 \2', self.body_text)

    @property
    def og_image(self):
        image = {'image': None, 'type': None}
        if self.feed_image:
            image['image'] = self.feed_image
        name, extension = os.path.splitext(image['image'].file.url)
        image['type'] = extension[1:]
        return image

    class Meta:
        description = "Article page for your site"
        verbose_name = "Article page"

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('date'),
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "SEO and metadata fields"),
        ImageChooserPanel('feed_image'),
    ]
