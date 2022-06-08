# from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
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
    print(context)
    return render(request, 'mainapp/elements/main_page.html', context)
