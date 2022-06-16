# from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from adminapp.models import *


def main_page(request):
    main_page_info = MainPage.objects.last()
    seo_block = SeoBlock.objects.get(pk=main_page_info.seo_block.pk)
    today = date.today()
    current_movies = Movie.objects.filter(start_sale__lte=today)
    coming_movies = Movie.objects.filter(start_sale__gt=today)

    background = BackgroundBanner.objects.last()
    top_banners = MainTopBanners.objects.all()
    news = MainNewsAndPromotionsBanners.objects.all()
    t_b_settings = BannersSettings.objects.get(settings_for='top_banners')
    n_p_settings = BannersSettings.objects.get(settings_for='news-promotions_banners')

    context = {
        'main_page_info': main_page_info,
        'seo_block': seo_block,
        'current_movies': current_movies,
        'coming_movies': coming_movies,
        'background': background,
        'top_banners': top_banners,
        'news': news,
        't_b_settings': t_b_settings,
        'n_p_settings': n_p_settings,
    }
    return render(request, 'mainapp/elements/main_page.html', context)


class PosterView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'mainapp/elements/movies.html'

    def get_queryset(self):
        today = date.today()
        return Movie.objects.filter(start_sale__lte=today)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_filter'] = 'today'
        return context


class SoonView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'mainapp/elements/movies.html'

    def get_queryset(self):
        today = date.today()
        return Movie.objects.filter(start_sale__gt=today)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_filter'] = 'soon'
        return context


class CinemasView(ListView):
    context_object_name = 'cinemas'
    template_name = 'mainapp/elements/cinemas.html'

    def get_queryset(self):
        return Cinema.objects.filter(is_active=True)


class ContactsView(ListView):
    model = CinemaContacts
    template_name = 'mainapp/pages/about/contacts.html'


class BasePageView(TemplateView):
    template_name = 'mainapp/pages/about/base_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = SitePage.objects.get(type=kwargs['type'])
        context['page_content'] = page_obj
        context['page_gallery'] = Image.objects.filter(gallery=page_obj.gallery.pk)
        context['seo_block'] = SeoBlock.objects.get(pk=page_obj.seo_block.pk)
        return context


def article_view(request):
    article_type = None
    if request.get_full_path().find('promotions') != -1:
        article_type = 'promotions'
    elif request.get_full_path().find('news') != -1:
        article_type = 'news'

    articles = Articles.objects.filter(article_type=article_type)
    context = {
        'articles': articles,
        'articles_type': article_type,
    }
    return render(request, 'mainapp/elements/articles.html', context)

# class ArticleView(ListView):
#     context_object_name = 'articles'
#
#     def get_queryset(self):
#         article_type = self.content_type()
#         print(Articles.objects.filter(article_type=article_type))
#         return Articles.objects.filter(article_type=article_type)
#
#     def content_type(self):
#         urls = ('promotions', 'news')
#         for e in urls:
#             if self.request.get_full_path().find(e) == -1:
#                 continue
#             return e
