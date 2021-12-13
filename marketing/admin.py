from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'timeStamp']


@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ['email', 'time']

# @admin.register(MainContent)
# class MainContentAdmin(admin.ModelAdmin):
#     list_display = ['content']

admin.site.register(MainContent)
admin.site.register(About)
admin.site.register(Resume)
admin.site.register(AboutSocial)
admin.site.register(FooterSocial)
admin.site.register(Aboutbulletin)


