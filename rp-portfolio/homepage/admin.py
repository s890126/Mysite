from django.contrib import admin
from homepage.models import Home

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    pass



admin.site.register(Home, HomeAdmin)
