from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Movie)
class MovieTranslationOption(TranslationOptions):
    fields = ('title', 'text')
    required_languages = ('uk',)


@register(Cinema)
class CinemaTranslationOption(TranslationOptions):
    fields = ('title', 'text', 'condition')
    required_languages = ('uk',)


@register(Hall)
class HallTranslationOption(TranslationOptions):
    fields = ('title', 'text')
    required_languages = ('uk',)


@register(Articles)
class ArticlesTranslationOption(TranslationOptions):
    fields = ('title', 'text')
    required_languages = ('uk',)


@register(MainPage)
class MainPageTranslationOption(TranslationOptions):
    fields = ('main_seo_text',)
    required_languages = ('uk',)


@register(SitePage)
class SitePageTranslationOption(TranslationOptions):
    fields = ('title', 'text')
    required_languages = ('uk',)


@register(CinemaContacts)
class CinemaContactsTranslationOption(TranslationOptions):
    fields = ('title', 'address')
    required_languages = ('uk',)
