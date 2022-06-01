from django.contrib import admin
from .models import *

# Models, for used image formset
admin.site.register(Gallery)
admin.site.register(Image)

admin.site.register(SeoBlock)

# Models for banners page and settings
admin.site.register(MainTopBanners)
admin.site.register(BackgroundBanner)
admin.site.register(MainNewsAndPromotionsBanners)
admin.site.register(BannersSettings)

admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(Hall)
admin.site.register(Session)

admin.site.register(Articles)

# Models for base site page
admin.site.register(MainPage)
admin.site.register(SitePage)
admin.site.register(CinemaContacts)

