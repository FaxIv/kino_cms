from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from .forms import MovieForm, ImageForm
from .models import *


def base(request):
    return render(request, "adminapp/elements/base.html")


def banners(request):
    return render(request, "adminapp/elements/banners.html")


def movies(request):
    movie = Movie.objects.all()
    context = {
        'movie': movie,
    }
    return render(request, "adminapp/elements/movies.html", context)


def cinemas(request):
    return render(request, "adminapp/elements/cinemas.html")


def news(request):
    return render(request, "adminapp/elements/news.html")


def promotions(request):
    return render(request, "adminapp/elements/promotions.html")


def pages(request):
    return render(request, "adminapp/elements/pages_base.html")


def mailing(request):
    return render(request, "adminapp/elements/mailing.html")


def movie_create(request):
    error = ''

    images = Image.objects.none()
    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    form = MovieForm(request.POST or None, prefix='movie')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')

    if request.method == 'POST':

        if form.is_valid() and image_forms.is_valid():
            movie_gallery = Gallery()
            movie_gallery.save()

            # Block set gallery obj. in image note
            for i_form in image_forms:
                if i_form.cleaned_data:
                    note = i_form.save(commit=False)
                    note.gallery = movie_gallery
                    note.save()

            f = form.save(commit=False)
            f.gallery = movie_gallery
            f.save()
            return redirect('/adminapp/movies')
        else:
            error = 'Дані хибні'

    context = {
        'form': form,
        'image_forms': image_forms,
        'error': error,
    }
    return render(request, 'adminapp/pages/movies/movie_page.html', context)


def movie_update(request, pk):
    error = ''

    image_formset = modelformset_factory(Image, form=ImageForm, extra=0, can_delete=True)
    model = Movie.objects.get(pk=pk)
    images = Image.objects.filter(gallery=model.gallery.pk)

    form = MovieForm(request.POST or None, request.FILES or None, instance=model, prefix='form')
    image_forms = image_formset(request.POST or None, request.FILES or None, queryset=images, prefix='images')

    if request.method == 'POST':
        if form.is_valid() and image_forms.is_valid():
            movie_gallery = Gallery.objects.get(pk=model.gallery.pk)

            for i_form in image_forms:
                if i_form.cleaned_data:
                    note = i_form.save(commit=False)
                    note.gallery = movie_gallery
                    note.save()

            image_forms.save()
            form.save()
            return redirect('/adminapp/movies')
        else:
            # TODO: add messages framework support
            error = 'Дані хибні'
    context = {
        'form': form,
        'image_forms': image_forms,
        'error': error,
    }
    return render(request, 'adminapp/pages/movies/movie_page.html', context)


def movie_delete(request, pk):
    model = Movie.objects.get(pk=pk)
    movie_gallery = Gallery.objects.get(pk=model.gallery.pk)
    if request.method == 'POST':
        movie_gallery.delete()
        return redirect('/adminapp/movies')
    else:
        return render(request, 'adminapp/pages/movies/movie_delete.html')


# # test upload some image with demonstrate them, can be deleted
# def image_upload_view(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj = form.instance
#             context = {
#                 'form': form,
#                 'img_obj': img_obj,
#             }
#             return render(request, 'adminapp/pages/movies/img.html', context)
#     else:
#         form = ImageForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'adminapp/pages/movies/img.html', context)
