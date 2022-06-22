from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import date
from .forms import *
from .models import *


@user_passes_test(lambda user: user.is_staff, redirect_field_name=None, login_url='main_page')
def base(request):
    return render(request, "adminapp/elements/welcome_page.html")


@user_passes_test(lambda user: user.is_staff, login_url='welcome-page')
def statistic(request):
    return render(request, "adminapp/elements/base.html")


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


@user_passes_test(lambda user: user.is_staff, login_url='welcome-page')
def banners(request):
    main_top_banners = MainTopBanners.objects.all()
    top_banners_formset = modelformset_factory(MainTopBanners, form=MainTopBannersForm, extra=0, can_delete=True)
    top_banners_forms = top_banners_formset(request.POST or None, request.FILES or None, queryset=main_top_banners,
                                            prefix='top_banner')

    background_banner = BackgroundBanner.objects.get(pk=1)
    background_banner_form = BackgroundBannerForm(request.POST or None, request.FILES or None,
                                                  instance=background_banner, prefix='background')

    main_news_promotions_banner = MainNewsAndPromotionsBanners.objects.all()
    news_promotion_banners_formset = modelformset_factory(MainNewsAndPromotionsBanners,
                                                          form=MainNewsAndPromotionsBannersForms, extra=0,
                                                          can_delete=True)
    news_promotion_banners_forms = news_promotion_banners_formset(request.POST or None, request.FILES or None,
                                                                  queryset=main_news_promotions_banner,
                                                                  prefix='news_promotions')

    t_b_settings = BannersSettings.objects.get(settings_for='top_banners')
    n_p_settings = BannersSettings.objects.get(settings_for='news-promotions_banners')
    t_b_settings_form = BannersSettingsForm(request.POST or None, instance=t_b_settings, prefix='t_b_settings')
    n_p_settings_form = BannersSettingsForm(request.POST or None, instance=n_p_settings, prefix='n_p_settings')
    print(request.POST)
    if request.method == 'POST':
        if is_ajax(request=request):
            if background_banner_form.is_valid():
                background_banner_form.save()
                print('work')
                return HttpResponse(status=200)
            else:
                print(f"Background ---> {background_banner_form.errors}")
                return HttpResponse(status=400)

        elif request.POST['save-button'] == 'top-banner-save':
            if top_banners_forms.is_valid() and t_b_settings_form.is_valid():
                print(top_banners_forms)
                top_banners_forms.save(commit=False)
                for form in top_banners_forms:
                    print(f"1 form --->: {form}")
                    if form.cleaned_data:
                        print(form)

                top_banners_forms.save()
                t_b_settings_form.save()
                return redirect('/adminapp/banners')
            else:
                print(f"Top banner ---> {top_banners_forms.errors}")
                print(f"Settings ---> {t_b_settings_form.errors}")
                messages.error(request, 'Дані хибні')

        elif request.POST['save-button'] == 'news-promotions-save':
            if news_promotion_banners_forms.is_valid() and n_p_settings_form.is_valid():
                news_promotion_banners_forms.save()
                n_p_settings_form.save()
                return redirect('/adminapp/banners')
            else:
                print(f"News promotions ---> {news_promotion_banners_forms.errors}")
                print(f"Settings ---> {n_p_settings_form.errors}")
                messages.error(request, 'Дані хибні')

    context = {
        'top_banners_forms': top_banners_forms,
        'background': background_banner_form,
        'news_promotions_forms': news_promotion_banners_forms,
        't_b_settings': t_b_settings_form,
        'n_p_settings': n_p_settings_form,
    }
    return render(request, "adminapp/elements/banners.html", context)


# region cinema_view
@permission_required('adminapp.view_cinema', login_url='login')
def cinemas(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas,
    }
    return render(request, "adminapp/elements/cinemas.html", context)


@permission_required('adminapp.create_cinema', login_url='login')
def cinema_create(request):
    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = CinemaForm(request.POST or None, request.FILES or None, prefix='cinema')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    seo_form = SeoBlockForm(request.POST or None, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            print(image_forms)
            this_gallery = Gallery.objects.create()
            save_image_formset(image_forms, this_gallery)

            this_seo = seo_form.save()

            f = form.save(commit=False)
            f.gallery = this_gallery
            f.seo_block = this_seo
            f.save()

            messages.success(request, f"Кінотеатр '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/cinemas')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, "Дані хибні")
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/cinemas/cinema_page.html", context)


@permission_required('adminapp.change_cinema', login_url='login')
def cinema_update(request, pk):
    model = Cinema.objects.get(pk=pk)
    seo_model = SeoBlock.objects.get(pk=model.seo_block.pk)
    images = Image.objects.filter(gallery=model.gallery.pk)
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = CinemaForm(request.POST or None, request.FILES or None, instance=model, prefix='cinema')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    halls = Hall.objects.filter(cinema=pk)
    seo_form = SeoBlockForm(request.POST or None, instance=seo_model, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            print(image_forms)
            this_gallery = Gallery.objects.get(pk=model.gallery.pk)

            save_image_formset(image_forms, this_gallery)
            form.save()
            seo_form.save()

            messages.success(request, f"Кінотеатр '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/cinemas')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, f'Дані хибні!')
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
        'halls': halls,
    }
    return render(request, "adminapp/pages/cinemas/cinema_page.html", context)


@permission_required('adminapp.delete_cinema', login_url='login')
def cinema_delete(request, pk):
    model = Cinema.objects.get(pk=pk)
    this_gallery = Gallery.objects.get(pk=model.gallery.pk)
    this_seo = SeoBlock.objects.get(pk=model.seo_block.pk)
    if request.method == 'POST':
        this_seo.delete()
        this_gallery.delete()
        messages.success(request, f"Кінотеатр '{model.title}' було видалено!")
        return redirect('/adminapp/cinemas')
    else:
        return render(request, 'adminapp/pages/cinemas/cinema_delete.html')


# endregion cinema_view

# region hall
@permission_required('adminapp.create_hall', login_url='login')
def hall_create(request, cinema_pk):
    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = HallForm(request.POST or None, request.FILES or None, prefix='hall')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    seo_form = SeoBlockForm(request.POST or None, prefix='seo')
    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            # hall_gallery = get_gallery()
            this_gallery = Gallery.objects.create()
            save_image_formset(image_forms, this_gallery)

            cinema = Cinema.objects.get(pk=cinema_pk)
            this_seo = seo_form.save()

            f = form.save(commit=False)
            f.cinema = cinema
            f.gallery = this_gallery
            f.seo_block = this_seo
            f.save()

            messages.success(request, f"Зал '{form.instance.title}' успішно збережено.")
            return redirect(f'/adminapp/cinemas/{cinema_pk}/cinema_update')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, "Дані хибні ")
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/halls/hall_page.html", context)


@permission_required('adminapp.change_hall', login_url='login')
def hall_update(request, cinema_pk, pk):
    model = Hall.objects.get(pk=pk)
    seo_model = SeoBlock.objects.get(pk=model.seo_block.pk)
    images = Image.objects.filter(gallery=model.gallery.pk)
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = HallForm(request.POST or None, request.FILES or None, instance=model, prefix='hall')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    seo_form = SeoBlockForm(request.POST or None, instance=seo_model, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            # hall_gallery = get_gallery(model)
            this_gallery = Gallery.objects.get(pk=model.gallery.pk)

            save_image_formset(image_forms, this_gallery)
            form.save()
            seo_form.save()

            messages.success(request, f"Зал '{form.instance.title}' успішно збережено.")
            return redirect(f'/adminapp/cinemas/{cinema_pk}/cinema_update')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, "Дані хибні")
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/halls/hall_page.html", context)


@permission_required('adminapp.delete_hall', login_url='login')
def hall_delete(request, cinema_pk, pk):
    model = Hall.objects.get(pk=pk)
    this_gallery = Gallery.objects.get(pk=model.gallery.pk)
    this_seo = SeoBlock.objects.get(pk=model.seo_block.pk)
    if request.method == 'POST':
        this_gallery.delete()
        this_seo.delete()
        messages.success(request, f"Зал '{model.title}' було видалено!")
        return redirect(f'/adminapp/cinemas/{cinema_pk}/cinema_update')
    else:
        return render(request, 'adminapp/pages/halls/hall_delete.html')


# endregion hall


# region news/promo
@permission_required('adminapp.view_articles', login_url='login')
def news(request):
    news_note = Articles.objects.filter(article_type='news')
    context = {
        'news': news_note,
    }
    return render(request, "adminapp/elements/news.html", context)


@permission_required('adminapp.view_articles', login_url='login')
def promotions(request):
    promotions_note = Articles.objects.filter(article_type='promotions')
    context = {
        'promotions': promotions_note,
    }
    return render(request, "adminapp/elements/promotions.html", context)


@permission_required('adminapp.create_articles', login_url='login')
def article_create(request, article_type):
    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = ArticleForm(request.POST or None, request.FILES or None, prefix='article')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    seo_form = SeoBlockForm(request.POST or None, prefix='seo')
    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            this_gallery = get_gallery()
            save_image_formset(image_forms, this_gallery)

            this_seo = seo_form.save()

            f = form.save(commit=False)
            f.article_type = article_type
            f.gallery = this_gallery
            f.seo_block = this_seo
            f.save()

            messages.success(request, f"Запис '{form.instance.title}' успішно збережено.")
            return redirect(f"/adminapp/{article_type}")
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, "Дані хибні")
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/articles/article_page.html", context)


@permission_required('adminapp.change_articles', login_url='login')
def article_update(request, article_type, pk):
    model = Articles.objects.get(pk=pk)
    seo_model = SeoBlock.objects.get(pk=model.seo_block.pk)
    images = Image.objects.filter(gallery=model.gallery.pk)
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = ArticleForm(request.POST or None, request.FILES or None, instance=model, prefix='article')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    seo_form = SeoBlockForm(request.POST or None, instance=seo_model, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            this_gallery = Gallery.objects.get(pk=model.gallery.pk)

            save_image_formset(image_forms, this_gallery)
            form.save()
            seo_form.save()

            messages.success(request, f"Запис '{form.instance.title}' успішно збережено.")
            return redirect(f"/adminapp/{article_type}")
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, 'Дані хибні!')
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/articles/article_page.html", context)


@permission_required('adminapp.delete_articles', login_url='login')
def article_delete(request, article_type, pk):
    model = Articles.objects.get(pk=pk)
    this_gallery = Gallery.objects.get(pk=model.gallery.pk)
    this_seo = SeoBlock.objects.get(pk=model.seo_block.pk)
    if request.method == 'POST':
        this_gallery.delete()
        this_seo.delete()
        messages.success(request, f"Запис '{model.title}' було видалено!")
        return redirect(f'/adminapp/{article_type}')
    context = {
        'article_type': article_type,
    }
    return render(request, "adminapp/pages/articles/article_delete.html", context)


# endregion news/promo


# region movie
@permission_required('adminapp.view_movie', login_url='login')
def movies(request):
    today = date.today()
    current_movies = Movie.objects.filter(start_sale__lte=today)
    coming_movies = Movie.objects.filter(start_sale__gt=today)

    context = {
        'current_movies': current_movies,
        'coming_movies': coming_movies,
    }
    return render(request, "adminapp/elements/movies.html", context)


@permission_required('adminapp.create_movie', login_url='login')
def movie_create(request):
    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = MovieForm(request.POST or None, request.FILES or None, prefix='movie')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    seo_form = SeoBlockForm(request.POST or None, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            this_gallery = Gallery.objects.create()
            save_image_formset(image_forms, this_gallery)

            this_seo = seo_form.save()

            f = form.save(commit=False)
            f.gallery = this_gallery
            f.seo_block = this_seo
            f.save()

            messages.success(request, f"Фільм '{form.instance.title}' успішно додано.")
            return redirect('/adminapp/movies')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, 'Дані хибні!')
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, 'adminapp/pages/movies/movie_page.html', context)


@permission_required('adminapp.change_movie', login_url='login')
def movie_update(request, pk):
    model = Movie.objects.get(pk=pk)
    seo_model = SeoBlock.objects.get(pk=model.seo_block.pk)
    images = Image.objects.filter(gallery=model.gallery.pk)
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    form = MovieForm(request.POST or None, request.FILES or None, instance=model, prefix='movie')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    seo_form = SeoBlockForm(request.POST or None, instance=seo_model, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            this_gallery = Gallery.objects.get(pk=model.gallery.pk)

            save_image_formset(image_forms, this_gallery)
            form.save()
            seo_form.save()

            messages.success(request, f"Фільм '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/movies')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, 'Дані хибні!')
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, 'adminapp/pages/movies/movie_page.html', context)


@permission_required('adminapp.delete_movie', login_url='login')
def movie_delete(request, pk):
    model = Movie.objects.get(pk=pk)
    this_gallery = Gallery.objects.get(pk=model.gallery.pk)
    this_seo = SeoBlock.objects.get(pk=model.seo_block.pk)
    if request.method == 'POST':
        this_seo.delete()
        this_gallery.delete()
        messages.success(request, f"Фільм '{model.title}' було видалено!")
        return redirect('/adminapp/movies')
    else:
        return render(request, 'adminapp/pages/movies/movie_delete.html')


# endregion movie

@permission_required('adminapp.view_sitepage', login_url='login')
def pages_base(request):
    main_page = get_object_or_404(MainPage, pk=1)
    pages = SitePage.objects.order_by('id')
    contacts = CinemaContacts.objects.first()
    if not contacts:
        contacts = CinemaContacts.objects.create()
    contacts_active = CinemaContacts.objects.all().filter(is_active__exact='True')
    print(contacts_active)
    context = {
        'main_page': main_page,
        'pages': pages,
        'contacts': contacts,
        'contacts_active': contacts_active,
    }
    return render(request, "adminapp/elements/pages_base.html", context)


@permission_required('adminapp.create_sitepage', login_url='login')
def pages_create(request):
    image = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=image, prefix='images')
    form = SitePageForm(request.POST or None, request.FILES or None, prefix='page')
    seo_form = SeoBlockForm(request.POST or None, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            # this_gallery = get_gallery()
            this_gallery = Gallery.objects.create()
            save_image_formset(image_forms, this_gallery)

            this_seo = seo_form.save()

            f = form.save(commit=False)
            f.gallery = this_gallery
            f.seo_block = this_seo
            f.save()

            messages.success(request, f"Сторінку '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/pages')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, "Дані хибні")
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/pagesbase/base_page.html", context)


@permission_required('adminapp.change_sitepage', login_url='login')
def pages_update(request, pk):
    model = SitePage.objects.get(pk=pk)
    seo_model = SeoBlock.objects.get(pk=model.seo_block.pk)
    images = Image.objects.filter(gallery=model.gallery.pk)
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    form = SitePageForm(request.POST or None, request.FILES or None, instance=model, prefix='page')
    seo_form = SeoBlockForm(request.POST or None, instance=seo_model, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid() and seo_form.is_valid():
            this_gallery = Gallery.objects.get(pk=model.gallery.pk)

            save_image_formset(image_forms, this_gallery)
            form.save()
            seo_form.save()

            messages.success(request, f"Сторінку '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/pages')
        else:
            print(form.errors)
            print(image_forms.errors)
            print(seo_form.errors)
            messages.error(request, "Дані хибні")
    context = {
        'form': form,
        'image_forms': image_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/pagesbase/base_page.html", context)


@permission_required('adminapp.delete_sitepage', login_url='login')
def pages_delete(request, pk):
    model = SitePage.objects.get(pk=pk)
    this_gallery = Gallery.objects.get(pk=model.gallery.pk)
    this_seo = SeoBlock.objects.get(pk=model.seo_block.pk)
    if request.method == 'POST':
        this_seo.delete()
        this_gallery.delete()
        messages.success(request, f"Сторінку '{model.title}' було видалено!")
        return redirect('/adminapp/pages')
    else:
        return render(request, 'adminapp/pages/pagesbase/base_page_delete.html')


@permission_required('adminapp.change_mainpage', login_url='login')
def main_page_update(request):
    model = MainPage.objects.get(pk=1)
    seo_model = SeoBlock.objects.get(pk=model.seo_block.pk)

    form = MainPageForm(request.POST or None, request.FILES or None, instance=model, prefix='page')
    seo_form = SeoBlockForm(request.POST or None, instance=seo_model, prefix='seo')

    if request.method == 'POST':
        if form.is_valid() and seo_form.is_valid():

            form.save()
            seo_form.save()

            messages.success(request, f"Головну сторінку успішно збережено.")
            return redirect('/adminapp/pages')
        else:
            print(form.errors)
            print(seo_form.errors)
            messages.error(request, "Дані хибні")
    context = {
        'form': form,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/pagesbase/main_page.html", context)


@permission_required('adminapp.change_cinemacontacts', login_url='login')
def cinema_contacts_update(request):
    contacts = CinemaContacts.objects.all()
    if contacts[0].seo_block is None:
        seo_model = SeoBlock.objects.create()
    else:
        seo_model = SeoBlock.objects.get(pk=contacts[0].seo_block.pk)

    contacts_formset = modelformset_factory(CinemaContacts, form=CinemaContactsForm, extra=0, can_delete=True)
    contact_forms = contacts_formset(request.POST or None, request.FILES or None, queryset=contacts, prefix='contact')
    seo_form = SeoBlockForm(request.POST or None, instance=seo_model, prefix='seo')
    print(request.POST)
    if request.method == 'POST':
        if contact_forms.is_valid() and seo_form.is_valid():

            contact_forms.save(commit=False)
            for c_form in contact_forms:
                if c_form.cleaned_data:
                    c_form.instance.seo_block = seo_model
            for elem in contact_forms.deleted_objects:
                elem.delete()
            contact_forms.save()

            seo_form.save()

            messages.success(request, f"Контакти кінтоеатрів успішно збережено.")
            return redirect('/adminapp/pages')
        else:
            print(f"contact-eror --- {contact_forms.errors}")
            print(f"seo-eror --- {seo_form.errors}")
            messages.error(request, "Дані хибні")
    context = {
        'contact_forms': contact_forms,
        'seo_form': seo_form,
    }
    return render(request, "adminapp/pages/pagesbase/cinema_contacts.html", context)


def get_gallery(model=None):
    if model:
        some_gallery = Gallery.objects.get(pk=model.gallery.pk)
        return some_gallery
    else:
        some_gallery = Gallery()
        some_gallery.save()
        return some_gallery


def save_image_formset(image_forms, some_gallery):
    image_forms.save(commit=False)
    for i_form in image_forms:
        if i_form.cleaned_data:
            i_form.instance.gallery = some_gallery
    for elem in image_forms.deleted_objects:
        elem.delete()
    image_forms.save()
