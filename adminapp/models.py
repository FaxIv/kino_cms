from django.db import models
from django.template.defaultfilters import date


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


class AbstractPage(models.Model):
    is_active = models.BooleanField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    main_image = models.ImageField(null=True, blank=True)
    seo_url = models.URLField()
    seo_title = models.CharField(max_length=50)
    seo_keywords = models.TextField()
    seo_description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def main_image_url(self):
        if self.main_image and hasattr(self.main_image, 'url'):
            return self.main_image.url
        else:
            return "/media/bsimg.jpeg"

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class AbstractProperties(models.Model):
    flag_3d = models.BooleanField(verbose_name='3D')
    flag_2d = models.BooleanField(verbose_name='2D')
    flag_imax = models.BooleanField(verbose_name='IMAX')

    class Meta:
        abstract = True


# Base pages site (about, cafe, children's room, VIP hall, advertising).

class BaseSitePage(AbstractPage):
    type = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Base pages'
        verbose_name = 'Base page'


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

class Articles(BaseSitePage):
    video_url = models.URLField(verbose_name='Video')
    date_publication = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'News and promotions'
        verbose_name = 'News and promotion'
