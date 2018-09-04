from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','Last_name', 'First_name']
    list_display_links = ['First_name']
    list_editable = ['Last_name']
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)

