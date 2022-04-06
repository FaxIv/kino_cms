from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# from .forms import MovieForm


# next two views test, can be deleted
def films(request):
    template = loader.get_template('adminapp/films.html')
    return HttpResponse(template.render())


def film_page(request):
    template = loader.get_template('adminapp/film_page.html')
    return HttpResponse(template.render())


# Views for cinemas
# def cinema_page(request):
#     template = loader.get_template('adminapp/cinema_page.html')
#     return HttpResponse(template.render())

# def cinema_page(request):
#     form = MovieForm()
#     data = {
#         'form': form
#     }
#     return render(request, 'adminapp/cinema_page.html', data)
