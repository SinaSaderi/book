from django.db import models
from django.utils.translation import gettext as _
from djangocms_text_ckeditor.fields import HTMLField

class Author(models.Model):
    full_name = models.CharField(_("Full name"), max_length=200)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return str(self.full_name)


class Translator(models.Model):
    full_name = models.CharField(_("Full name"), max_length=200)

    class Meta:
        verbose_name = _("Translator")
        verbose_name_plural = _("Translators")

    def __str__(self):
        return str(self.full_name)


class Publication(models.Model):
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.title)

class Article(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    author = models.ForeignKey(Author, verbose_name=_("Author"))
    translator = models.ForeignKey(Translator, verbose_name=_("Translator"), blank=True, null=True)
    place = models.CharField(_("Title"), max_length=200, blank=True, null=True)
    year = models.CharField(_("Year"), max_length=20, blank=True, null=True)
    page = models.CharField(_("Page"), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return str(self.title)