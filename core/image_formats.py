from wagtail.wagtailimages.formats import Format, register_image_format

register_image_format(Format('original', 'Original', 'richtext-image original', 'original'))
