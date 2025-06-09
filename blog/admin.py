from django.contrib import admin

from .models import Post

class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('date',)

admin.site.register(Post, BlogAdmin)