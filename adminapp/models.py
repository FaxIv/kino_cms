from django.db import models


class Gallery(models.Model):
    pass


class Image(models.Model):
    image = models.ImageField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Images'
        verbose_name = 'Image'


class AbstractPage(models.Model):
    is_active = models.BooleanField()
    title = models.CharField(max_length=50)
    text = models.TextField()
    seo_url = models.URLField()
    seo_title = models.CharField(max_length=50)
    seo_keywords = models.CharField(max_length=80)
    seo_description = models.TextField()
    date_created = models.DateField()
    date_updated = models.DateField()
    gallery = models.ForeignKey(Gallery, on_delete=models.PROTECT)

    class Meta:
        abstract = True


# Base pages site (about, cafe, children's room, VIP hall, advertising).

class BaseSitePage(AbstractPage):
    type = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Base pages'
        verbose_name = 'Base page'


# Models for all movies.

class Movie(AbstractPage):
    trailer_url = models.URLField()
    duration = models.PositiveSmallIntegerField()
    flag_3d = models.BooleanField(verbose_name='3D')
    flag_2d = models.BooleanField(verbose_name='2D')
    flag_imax = models.BooleanField(verbose_name='IMAX')
    start_sale = models.DateField()
    finish_sale = models.DateField()

    class Meta:
        verbose_name_plural = 'Movies'
        verbose_name = 'Movie'


# Models for all cinemas.

class Cinema(AbstractPage):
    condition = models.TextField()

    class Meta:
        verbose_name_plural = 'Cinemas'
        verbose_name = 'Cinema'


# Models for hall.

class Hall(AbstractPage):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    seats_config = models.CharField(max_length=50, verbose_name='Simple seats config')
    vip_seats_config = models.CharField(max_length=50, verbose_name='VIP seats config')
    flag_3d = models.BooleanField(verbose_name='3D')
    flag_2d = models.BooleanField(verbose_name='2D')
    flag_imax = models.BooleanField(verbose_name='IMAX')

    class Meta:
        verbose_name_plural = 'Halls'
        verbose_name = 'Hall'


# Models for sessions pages and reserved page

class Session(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    start = models.DateTimeField()
    flag_3d = models.BooleanField(verbose_name='3D')
    flag_2d = models.BooleanField(verbose_name='2D')
    flag_imax = models.BooleanField(verbose_name='IMAX')
    seats_reserved = models.CharField(max_length=50)
    seats_busy = models.CharField(max_length=50)

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

