from django.contrib import admin
from .models import CharityItem


# Register your models here.



class CharityItemAdmin(admin.ModelAdmin):

    list_display = ('charity_title', 'charity_short_description', 'upload_date')

admin.site.register(CharityItem, CharityItemAdmin)