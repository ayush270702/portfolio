from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Resume)
admin.site.register(models.Education)
admin.site.register(models.Skills)
admin.site.register(models.Services)
admin.site.register(models.Projects)

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name','mail','phone','message','time')


admin.site.register(models.Contact, ContactAdmin)