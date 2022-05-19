import datetime
from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .forms import *
from .models import *


def base(request):
    return render(request, "adminapp/elements/base.html")


def banners(request):
    return render(request, "adminapp/elements/banners.html")


def cinemas(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas,
    }
    return render(request, "adminapp/elements/cinemas.html", context)


def cinema_create(request):
    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    form = CinemaForm(request.POST or None, request.FILES or None, prefix='cinema')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            cinema_gallery = get_gallery()
            save_image_formset(image_forms, cinema_gallery)

            f = form.save(commit=False)
            f.gallery = cinema_gallery
            f.save()

            messages.success(request, f"Кінотеатр '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/cinemas')
        else:
            print(form.errors)
            print(image_forms.errors)
            messages.error(request, f"Дані хибні {form.errors, image_forms.errors}")
    context = {
        'form': form,
        'image_forms': image_forms
    }
    return render(request, "adminapp/pages/cinemas/cinema_page.html", context)


def cinema_update(request, pk):
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    model = Cinema.objects.get(pk=pk)
    images = Image.objects.filter(gallery=model.gallery.pk)

    form = CinemaForm(request.POST or None, request.FILES or None, instance=model, prefix='cinema')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    halls = Hall.objects.filter(cinema=pk)

    print(form.instance.id)
    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            cinema_gallery = get_gallery(model)
            save_image_formset(image_forms, cinema_gallery)

            form.save()
            messages.success(request, f"Кінотеатр '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/cinemas')
        else:
            print(form.errors)
            print(image_forms.errors)
            messages.error(request, 'Дані хибні!')

    context = {
        'form': form,
        'image_forms': image_forms,
        'halls': halls,
    }
    return render(request, "adminapp/pages/cinemas/cinema_page.html", context)


def cinema_delete(request, pk):
    model = Cinema.objects.get(pk=pk)
    cinema_gallery = get_gallery(model)
    if request.method == 'POST':
        cinema_gallery.delete()
        messages.success(request, f"Кінотеатр '{model.title}' було видалено!")
        return redirect('/adminapp/cinemas')
    else:
        return render(request, 'adminapp/pages/cinemas/cinema_delete.html')


def hall_create(request, cinema_pk):
    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)

    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    form = HallForm(request.POST or None, request.FILES or None, prefix='hall')
    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            hall_gallery = get_gallery()
            save_image_formset(image_forms, hall_gallery)

            cinema = Cinema.objects.get(pk=cinema_pk)
            f = form.save(commit=False)
            f.cinema = cinema
            f.gallery = hall_gallery
            f.save()

            messages.success(request, f"Зал '{form.instance.title}' успішно збережено.")
            return redirect(f'/adminapp/cinemas/{cinema_pk}/cinema_update')
        else:
            print(form.errors)
            print(image_forms.errors)
            messages.error(request, f"Дані хибні {form.errors, image_forms.errors}")
    context = {
        'form': form,
        'image_forms': image_forms,
    }

    return render(request, "adminapp/pages/halls/hall_page.html", context)


def hall_update(request, cinema_pk, pk):
    model = Hall.objects.get(pk=pk)
    form = HallForm(request.POST or None, request.FILES or None, instance=model, prefix='hall')

    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    images = Image.objects.filter(gallery=model.gallery.pk)
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            hall_gallery = get_gallery(model)
            save_image_formset(image_forms, hall_gallery)
            form.save()

            messages.success(request, f"Зал '{form.instance.title}' успішно збережено.")
            return redirect(f'/adminapp/cinemas/{cinema_pk}/cinema_update')
        else:
            print(form.errors)
            print(image_forms.errors)
            messages.error(request, f"Дані хибні {form.errors, image_forms.errors}")

    context = {
        'form': form,
        'image_forms': image_forms,
    }
    return render(request, "adminapp/pages/halls/hall_page.html", context)


def hall_delete(request, cinema_pk, pk):
    model = Hall.objects.get(pk=pk)
    hall_gallery = get_gallery(model)
    if request.method == 'POST':
        hall_gallery.delete()
        messages.success(request, f"Зал '{model.title}' було видалено!")
        return redirect(f'/adminapp/cinemas/{cinema_pk}/cinema_update')
    else:
        return render(request, 'adminapp/pages/halls/hall_delete.html')


def news(request):
    return render(request, "adminapp/elements/news.html")


def promotions(request):
    return render(request, "adminapp/elements/promotions.html")


def mailing(request):
    return render(request, "adminapp/elements/mailing.html")


def movies(request):
    today = datetime.date.today()
    current_movies = Movie.objects.filter(start_sale__lte=today)
    coming_movies = Movie.objects.filter(start_sale__gt=today)

    context = {
        'current_movies': current_movies,
        'coming_movies': coming_movies,
    }
    return render(request, "adminapp/elements/movies.html", context)


def movie_create(request):
    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    form = MovieForm(request.POST or None, request.FILES or None, prefix='movie')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            movie_gallery = get_gallery()
            save_image_formset(image_forms, movie_gallery)

            f = form.save(commit=False)
            f.gallery = movie_gallery
            f.save()
            messages.success(request, f"Фільм '{form.instance.title}' успішно додано.")
            return redirect('/adminapp/movies')
        else:
            print(form.errors)
            messages.error(request, 'Дані хибні!')
    context = {
        'form': form,
        'image_forms': image_forms,
    }
    return render(request, 'adminapp/pages/movies/movie_page.html', context)


def movie_update(request, pk):
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    model = Movie.objects.get(pk=pk)
    images = Image.objects.filter(gallery=model.gallery.pk)

    form = MovieForm(request.POST or None, request.FILES or None, instance=model, prefix='movie')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            # movie_gallery = Gallery.objects.get(pk=model.gallery.pk)
            # print(f"Base gallery method: {movie_gallery}")
            # gall = get_gallery(model)
            # print(f"New gallery method: {gall}")
            movie_gallery = get_gallery(model)

            # image_forms.save(commit=False)
            # for i_form in image_forms:
            #     if i_form.cleaned_data:
            #         i_form.instance.gallery = movie_gallery
            # for elem in image_forms.deleted_objects:
            #     elem.delete()
            # image_forms.save()
            save_image_formset(image_forms, movie_gallery)

            form.save()
            messages.success(request, f"Фільм '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/movies')
        else:
            print(form.errors)
            messages.error(request, 'Дані хибні!')
    context = {
        'form': form,
        'image_forms': image_forms,
    }
    return render(request, 'adminapp/pages/movies/movie_page.html', context)


def movie_delete(request, pk):
    model = Movie.objects.get(pk=pk)
    movie_gallery = Gallery.objects.get(pk=model.gallery.pk)
    if request.method == 'POST':
        movie_gallery.delete()
        messages.success(request, f"Фільм '{model.title}' було видалено!")
        return redirect('/adminapp/movies')
    else:
        return render(request, 'adminapp/pages/movies/movie_delete.html')


def pages_base(request):
    pages = BaseSitePage.objects.all()
    context = {
        'pages': pages,
    }
    return render(request, "adminapp/elements/pages_base.html", context)


def pages_create(request):
    pages = BaseSitePage.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=pages, prefix='images')
    form = BaseSitePageForm(request.POST or None, request.FILES or None, prefix='page')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            this_gallery = get_gallery()
            save_image_formset(image_forms, this_gallery)

            f = form.save(commit=False)
            f.gallery = this_gallery
            f.save()

            messages.success(request, f"Сторінку '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/pages')
        else:
            print(form.errors)
            print(image_forms.errors)
            messages.error(request, f"Дані хибні {form.errors, image_forms.errors}")
    context = {
        'form': form,
        'image_forms': image_forms
    }
    return render(request, "adminapp/pages/pagesbase/base_page.html", context)


def pages_update(request, pk):
    model = BaseSitePage.objects.get(pk=pk)
    images = Image.objects.filter(gallery=model.gallery.pk)
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')
    form = MovieForm(request.POST or None, request.FILES or None, instance=model, prefix='page')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            this_gallery = get_gallery(model)
            save_image_formset(image_forms, this_gallery)
            form.save()
            messages.success(request, f"Сторінку '{form.instance.title}' успішно збережено.")
            return redirect('/adminapp/pages')
        else:
            print(form.errors)
            print(image_forms.errors)
            messages.error(request, f"Дані хибні {form.errors, image_forms.errors}")
    context = {
        'form': form,
        'image_forms': image_forms
    }
    return render(request, "adminapp/pages/pagesbase/base_page.html", context)


def pages_delete(request, pk):
    model = BaseSitePage.objects.get(pk=pk)
    this_gallery = get_gallery(model)
    if request.method == 'POST':
        this_gallery.delete()
        messages.success(request, f"Сторінку '{model.title}' було видалено!")
        return redirect('/adminapp/pages')
    else:
        return render(request, 'adminapp/pages/pagesbase/base_page_delete.html')


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
