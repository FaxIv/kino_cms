from django.forms import ModelForm, TextInput, DateInput, Textarea, URLInput, CheckboxInput, NumberInput, HiddenInput, ImageField
from .models import *


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'flag_3d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_2d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_imax': CheckboxInput(attrs={'class': 'form-check-input'}),
            'trailer_url': URLInput(attrs={'class': 'form-control'}),
            'seo_url': URLInput(attrs={'class': 'form-control'}),
            'seo_title': TextInput(attrs={'class': 'form-control'}),
            'seo_keywords': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'seo_description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'duration': NumberInput(attrs={'class': 'form-control', 'placeholder': 'У хвилинах'}),
            'start_sale': DateInput(attrs={'class': 'form-control'}),
            'finish_sale': DateInput(attrs={'class': 'form-control'}),
            'date_created': DateInput(attrs={'class': 'form-control'}),
            'date_updated': DateInput(attrs={'class': 'form-control'}),
            'gallery': HiddenInput(),
        }


class ImageForm(ModelForm):

    # def save(self, commit=True):
    #     image = super(ImageForm, self).save(commit=False)


    class Meta:
        model = Image
        fields = '__all__'

        widgets = {
            'gallery': HiddenInput(),
        }


