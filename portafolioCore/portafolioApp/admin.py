from django.contrib import admin
from portafolioApp import models

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","image","link","created","update"]
    readonly_fields = ["created","update"]

admin.site.register(models.Project,ProjectAdmin)
 