from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from baseplugin.models import BasePlugin
from baseplugin.utils import get_str_from_tuple
from filer.fields.image import FilerImageField

from . import conf


@python_2_unicode_compatible
class Column(BasePlugin):
    bg_color = models.CharField(_('background color'), max_length=50,
                                blank=True, default='')
    bg_image = FilerImageField(verbose_name=_('background image'), null=True,
                               default=None, blank=True,
                               related_name='columns_column_bg_image_set',
                               on_delete=models.SET_NULL)

    def __str__(self):
        name = ''
        names = []
        if self.name:
            names.append(self.name)
        if self.width:
            width = get_str_from_tuple(self.width, conf.COLUMN_WIDTHS)
            names.append('| {0}'.format(width))
        if self.bg_color:
            names.append(get_str_from_tuple(self.bg_color,
                                            conf.COLUMN_BACKGROUND_COLORS))
        if self.css_class:
            names.append(get_str_from_tuple(self.css_class,
                                            conf.COLUMN_CSS_CLASSES))
        if not self.is_visible:
            names.append('| {0}'.format(_('(hidden)')))
        if names:
            name = ' '.join(names)
        return name
