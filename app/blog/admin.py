from django.contrib import admin
from django.db import models
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.conf import settings
AdminSite.site_title = ugettext_lazy(settings.ADMIN_TITLE)

from mdeditor.widgets import MDEditorWidget

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'desc', 'content', 'created')

    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }


admin.site.register(Article, ArticleAdmin)
