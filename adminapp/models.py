from django.db import models
from datetime import datetime


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Gallery'


class Image(models.Model):
    image = models.ImageField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/bsimg.jpeg"

    class Meta:
        verbose_name_plural = 'Images'
        verbose_name = 'Image'


class SeoBlock(models.Model):
    seo_url = models.URLField(null=True, blank=True)
    seo_title = models.CharField(max_length=100, null=True, blank=True)
    seo_keywords = models.TextField(null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)


class AbstractPage(models.Model):
    is_active = models.BooleanField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    main_image = models.ImageField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    seo_block = models.ForeignKey(SeoBlock, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def main_image_url(self):
        if self.main_image and hasattr(self.main_image, 'url'):
            return self.main_image.url
        else:
            return "/media/bsimg.jpeg"

    class Meta:
        abstract = True




class AbstractProperties(models.Model):
    flag_3d = models.BooleanField(verbose_name='3D')
    flag_2d = models.BooleanField(verbose_name='2D')
    flag_imax = models.BooleanField(verbose_name='IMAX')

    class Meta:
        abstract = True


# region banners
class BaseBannerModel(models.Model):
    banner_image = models.CharField()

    class Meta:
        abstract = True

    @property
    def banner_storage_url(self):
        if self.banner_image and hasattr(self.banner_image, 'url'):
            return self.banner_image.url
        else:
            return "/media/bsimg.jpeg"


class MainTopBanners(BaseBannerModel):
    banner_image = models.ImageField(upload_to='main/banners/top/', null=True, blank=True)
    banner_url = models.URLField(null=True, blank=True)
    banner_text = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Top banners on main page'
        verbose_name = 'Top banner'


class BackgroundBanner(BaseBannerModel):
    banner_image = models.ImageField(upload_to='main/banners/background/', null=True, blank=True)
    background_or_banner = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Background banner'
        verbose_name = 'Background banner'


class MainNewsAndPromotionsBanners(BaseBannerModel):
    banner_image = models.ImageField(upload_to='main/banners/news_and_promotions/', null=True, blank=True)
    banner_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'News and promotions banners'
        verbose_name = 'News/promotion banner'


class BannersSettings(models.Model):
    is_active_top_banner = models.BooleanField(default=False)
    speed_top_banner = models.PositiveSmallIntegerField(default=5)
    is_active_news_and_promotion = models.BooleanField(default=False)
    speed_news_and_promotion = models.PositiveSmallIntegerField(default=5)

    class Meta:
        verbose_name_plural = 'Banners page settings'
        verbose_name = 'Banners page setting'


# endregion banners


# Models for all movies.

class Movie(AbstractPage, AbstractProperties):
    trailer_url = models.URLField()
    duration = models.PositiveSmallIntegerField()
    start_sale = models.DateField()
    finish_sale = models.DateField()

    class Meta:
        verbose_name_plural = 'Movies'
        verbose_name = 'Movie'


# Models for all cinemas.

class Cinema(AbstractPage):
    top_banner_image = models.ImageField(null=True, blank=True)
    condition = models.TextField()

    @property
    def top_banner_image_url(self):
        if self.top_banner_image and hasattr(self.top_banner_image, 'url'):
            return self.top_banner_image.url
        else:
            return "/media/bsimg.jpeg"

    class Meta:
        verbose_name_plural = 'Cinemas'
        verbose_name = 'Cinema'


# Models for hall.

class Hall(AbstractPage, AbstractProperties):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, null=True, blank=True)
    seats_config = models.CharField(max_length=50, verbose_name='Simple seats config')
    vip_seats_config = models.CharField(max_length=50, null=True, blank=True, verbose_name='VIP seats config')

    class Meta:
        verbose_name_plural = 'Halls'
        verbose_name = 'Hall'


# Models for sessions pages and reserved page

class Session(AbstractProperties):
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    start = models.DateTimeField()
    seats_reserved = models.CharField(max_length=50, null=True, blank=True)
    seats_busy = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Sessions'
        verbose_name = 'Session'


# Models for news page and promotions page

class Articles(AbstractPage):
    article_type = models.CharField(max_length=20, null=True, blank=True)
    video_url = models.URLField(verbose_name='Video')
    date_publication = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'News and promotions'
        verbose_name = 'News and promotions'


# region base_pages
# Base pages site (about, cafe, children's room, VIP hall, advertising).
class MainPage(models.Model):
    is_active = models.BooleanField(default=False)
    phone_1 = models.CharField(max_length=25)
    phone_2 = models.CharField(max_length=25, null=True, blank=True)
    main_seo_text = models.TextField()
    seo_block = models.ForeignKey(SeoBlock, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Main page'
        verbose_name = 'Main page'


class SitePage(AbstractPage):
    non_delete_page = models.BooleanField(default=False)
    type = models.CharField(max_length=30, default='other_page', null=True, blank=True)
    seo_block = models.ForeignKey(SeoBlock, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Base pages'
        verbose_name = 'Base page'


class CinemaContacts(models.Model):
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    coordinates = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True)
    seo_block = models.ForeignKey(SeoBlock, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    @property
    def logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return "/media/bsimg.jpeg"

    class Meta:
        verbose_name_plural = 'Cinemas contacts'
        verbose_name = 'Cinema contacts'


# endregion
