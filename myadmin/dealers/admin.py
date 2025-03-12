from django.contrib import admin

# Register your models here.

from . models import Dealer

from import_export.admin import ImportExportActionModelAdmin

admin.site.register(Dealer, ImportExportActionModelAdmin)
