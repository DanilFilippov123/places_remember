from django.contrib import admin

from app.models import Place, UserProfile


# Register your models here.
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
