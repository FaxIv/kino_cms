from django.forms import ModelForm, TextInput, DateInput, Textarea, URLInput, CheckboxInput, NumberInput, HiddenInput, \
    ImageField
from .models import *


class ImageForm(ModelForm):
    image = ImageField()

    # def save(self, commit=True):
    #     image = super(ImageForm, self).save(commit=False)

    class Meta:
        model = Image
        fields = '__all__'

        widgets = {
            'gallery': HiddenInput(),
        }


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title': TextInput(attrs={'class': 'form-control form-inp'}),
            'text': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'flag_3d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_2d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_imax': CheckboxInput(attrs={'class': 'form-check-input'}),
            'trailer_url': URLInput(attrs={'class': 'form-control form-inp'}),
            'seo_url': URLInput(attrs={'class': 'form-control form-inp'}),
            'seo_title': TextInput(attrs={'class': 'form-control form-inp'}),
            'seo_keywords': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'seo_description': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'duration': NumberInput(attrs={'class': 'form-control form-inp', 'placeholder': 'У хвилинах'}),
            'start_sale': DateInput(attrs={'class': 'form-control form-inp', 'type': 'date'}),
            'finish_sale': DateInput(attrs={'class': 'form-control form-inp', 'type': 'date'}),
            'date_created': DateInput(attrs={'class': 'form-control'}),
            'date_updated': DateInput(attrs={'class': 'form-control'}),
            'gallery': HiddenInput(),
        }


# region cinema
class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        exclude = ('gallery',)

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'condition': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'seo_url': URLInput(attrs={'class': 'form-control'}),
            'seo_title': TextInput(attrs={'class': 'form-control'}),
            'seo_keywords': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'seo_description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'date_created': DateInput(attrs={'class': 'form-control'}),
            'date_updated': DateInput(attrs={'class': 'form-control'}),
        }


# endregion cinema
class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'seats_config': TextInput(attrs={'class': 'form-control'}),
            'vip_seats_config': TextInput(attrs={'class': 'form-control'}),
            'flag_3d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_2d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_imax': CheckboxInput(attrs={'class': 'form-check-input'}),
            'seo_url': URLInput(attrs={'class': 'form-control'}),
            'seo_title': TextInput(attrs={'class': 'form-control'}),
            'seo_keywords': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'seo_description': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'date_created': DateInput(attrs={'class': 'form-control'}),
            'date_updated': DateInput(attrs={'class': 'form-control'}),
            'gallery': HiddenInput(),
            'cinema': HiddenInput(),
        }


class BaseSitePageForm(ModelForm):
    class Meta:
        model = BaseSitePage
        fields = '__all__'

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'type': TextInput(attrs={'class': 'form-control form-inp'}),
            'title': TextInput(attrs={'class': 'form-control form-inp'}),
            'text': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'seo_url': URLInput(attrs={'class': 'form-control form-inp'}),
            'seo_title': TextInput(attrs={'class': 'form-control form-inp'}),
            'seo_keywords': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'seo_description': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'date_created': DateInput(attrs={'class': 'form-control'}),
            'date_updated': DateInput(attrs={'class': 'form-control'}),
            'gallery': HiddenInput(),
        }
