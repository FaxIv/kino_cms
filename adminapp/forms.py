# from django.forms import ModelForm, TextInput, DateTimeInput, DateInput, Textarea, URLInput, CheckboxInput
# from .models import *
#
#
# class MovieForm(ModelForm):
#
#     class Meta:
#         model = Movie
#         fields = ('title',
#                   'info',
#                   'trailer_url',
#                   'duration',
#                   'flag_3d',
#                   'flag_2d',
#                   'flag_imax',
#                   'start_sale',
#                   'finish_sale',
#                   'date_created',
#                   'date_updated',
#                   'gallery')
#
#         widgets = {
#             'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
#             'info': Textarea(attrs={'class': 'form-control', 'placeholder': 'Info'}),
#             'trailer_url': URLInput(attrs={'class': 'form-control'}),
#             'duration': TextInput(attrs={'class': 'form-control'}),
#             'flag_3d': CheckboxInput(attrs={}),
#             'flag_2d': CheckboxInput(attrs={}),
#             'flag_imax': CheckboxInput(attrs={}),
#             'start_sale': DateInput(attrs={'class': 'form-control'}),
#             'finish_sale': DateInput(attrs={'class': 'form-control'}),
#             'date_created': DateInput(attrs={'class': 'form-control'}),
#             'date_updated': DateInput(attrs={'class': 'form-control'}),
#         }
