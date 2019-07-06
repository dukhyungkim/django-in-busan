from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['updated_at']
    search_fields = ['title']