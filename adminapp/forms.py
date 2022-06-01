from django.forms import ModelForm, TextInput, DateInput, Textarea, URLInput, CheckboxInput, NumberInput, HiddenInput, \
    ImageField, DateTimeInput, Select
from django.utils.translation import gettext_lazy as _
from .models import *


class ImageForm(ModelForm):
    image = ImageField()

    class Meta:
        model = Image
        fields = '__all__'

        widgets = {
            'gallery': HiddenInput(),
        }


class SeoBlockForm(ModelForm):
    class Meta:
        model = SeoBlock
        fields = '__all__'

        widgets = {
            'seo_url': URLInput(attrs={'class': 'form-control form-inp'}),
            'seo_title': TextInput(attrs={'class': 'form-control form-inp'}),
            'seo_keywords': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'seo_description': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
        }


# region banners_page
class MainTopBannersForm(ModelForm):
    class Meta:
        model = MainTopBanners
        fields ='__all__'

        widgets = {
            'banner_url': URLInput(attrs={'class': 'form-control'}),
            'banner_text': TextInput(attrs={'class': 'form-control'}),
        }


class BackgroundBannerForm(ModelForm):
    class Meta:
        model = BackgroundBanner
        fields = '__all__'

        widgets = {
            'background_or_banner': TextInput(attrs={'class': 'form-control'}),
        }


class MainNewsAndPromotionsBannersForms(ModelForm):
    class Meta:
        model = MainNewsAndPromotionsBanners
        fields = '__all__'

        widgets = {
            'banner_url': URLInput(attrs={'class': 'form-control'}),
        }


class BannersSettingsForm(ModelForm):

    class Meta:
        model = BannersSettings
        fields = '__all__'

        SPEED = (
            ('5', '5'),
            ('10', '10'),
            ('15', '15'),
        )

        widgets = {
            'is_active_top_banner': CheckboxInput(attrs={'class': 'form-check-input'}),
            'speed_top_banner': Select(choices=SPEED, attrs={'class': 'form-control'}),
            'is_active_news_and_promotion': CheckboxInput(attrs={'class': 'form-check-input'}),
            'speed_news_and_promotion': Select(choices=SPEED, attrs={'class': 'form-control'}),
        }


# endregion

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('title', 'text', 'date_created', 'date_updated', 'gallery', 'seo_block')

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title_uk': TextInput(attrs={'class': 'form-control form-inp'}),
            'title_ru': TextInput(attrs={'class': 'form-control form-inp'}),
            'text_uk': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'text_ru': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'flag_3d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_2d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_imax': CheckboxInput(attrs={'class': 'form-check-input'}),
            'trailer_url': URLInput(attrs={'class': 'form-control form-inp'}),
            'duration': NumberInput(attrs={'class': 'form-control form-inp', 'placeholder': 'У хвилинах'}),
            'start_sale': DateInput(attrs={'class': 'form-control form-inp', 'type': 'date'}),
            'finish_sale': DateInput(attrs={'class': 'form-control form-inp', 'type': 'date'}),
        }


# region cinema
class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        exclude = ('title', 'text', 'condition', 'date_created', 'date_updated', 'gallery', 'seo_block')

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            # 'title': TextInput(attrs={'class': 'form-control'}),
            'title_uk': TextInput(attrs={'class': 'form-control', 'required': '', 'placeholder': _('Назва')}),
            'title_ru': TextInput(attrs={'class': 'form-control'}),
            # 'text': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'text_uk': Textarea(attrs={'class': 'form-control', 'rows': '3', 'required': ''}),
            'text_ru': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            # 'condition': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'condition_uk': Textarea(attrs={'class': 'form-control', 'rows': '3', 'required': ''}),
            'condition_ru': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


# endregion cinema

class HallForm(ModelForm):
    class Meta:
        model = Hall
        exclude = ('title', 'text', 'date_created', 'date_updated', 'gallery', 'cinema', 'seo_block')

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title_uk': TextInput(attrs={'class': 'form-control'}),
            'title_ru': TextInput(attrs={'class': 'form-control'}),
            'text_uk': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'text_ru': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'seats_config': TextInput(attrs={'class': 'form-control'}),
            'vip_seats_config': TextInput(attrs={'class': 'form-control'}),
            'flag_3d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_2d': CheckboxInput(attrs={'class': 'form-check-input'}),
            'flag_imax': CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        exclude = ('title', 'text', 'article_type', 'date_created', 'date_updated', 'gallery', 'seo_block')

        widgets = {
            'is_active': CheckboxInput(attrs={'class': ''}),
            'date_publication': DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'title_uk': TextInput(attrs={'class': 'form-control form-inp', 'required': ''}),
            'title_ru': TextInput(attrs={'class': 'form-control form-inp'}),
            'text_uk': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'text_ru': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'video_url': URLInput(attrs={'class': 'form-control form-inp'}),
        }


# region base_pages
class MainPageForm(ModelForm):
    class Meta:
        model = MainPage
        exclude = ('main_seo_text', 'seo_block',)

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'phone_1': TextInput(attrs={'class': 'form-control'}),
            'phone_2': TextInput(attrs={'class': 'form-control'}),
            'main_seo_text_uk': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'main_seo_text_ru': Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class SitePageForm(ModelForm):
    class Meta:
        model = SitePage
        exclude = ('title', 'text', 'non_delete_page', 'type', 'gallery', 'seo_block', 'date_created', 'date_updated',)

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title_uk': TextInput(attrs={'class': 'form-control form-inp'}),
            'title_ru': TextInput(attrs={'class': 'form-control form-inp'}),
            'text_uk': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
            'text_ru': Textarea(attrs={'class': 'form-control form-inp', 'rows': '3'}),
        }


class CinemaContactsForm(ModelForm):
    class Meta:
        model = SeoBlock
        exclude = ('id', 'title_uk', 'title_ru', 'address_uk', 'address_ru', 'seo_block',)

        widgets = {
            'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
            'title': TextInput(attrs={'class': 'form-control title-inp'}),
            'address': Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'coordinates': TextInput(attrs={'class': 'form-control form-inp'}),
        }


# class CinemaContactsForm(ModelForm):
#     class Meta:
#         model = SeoBlock
#         exclude = ('title', 'address', 'seo_block',)
#
#         widgets = {
#             'is_active': CheckboxInput(attrs={'class': 'form-check-input'}),
#             'title_uk': TextInput(attrs={'class': 'form-control form-inp'}),
#             'title_ru': TextInput(attrs={'class': 'form-control form-inp'}),
#             'address_uk': TextInput(attrs={'class': 'form-control form-inp'}),
#             'address_ru': TextInput(attrs={'class': 'form-control form-inp'}),
#             'coordinates': TextInput(attrs={'class': 'form-control form-inp'}),
#         }


# endregion

