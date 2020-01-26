from django.db import models
from django.utils.translation import ugettext_lazy as _

class Navigation(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"), unique=True)
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name=_("Slug"))
    parent_id = models.ForeignKey("self", verbose_name=_("Parent"))
    url = models.CharField(max_length=200, verbose_name=_("url"))

    class Meta:
        verbose_name = _("Navgation")
        verbose_name_plural = _("Navgations")

    def __str__(self):
        return str(self.title)