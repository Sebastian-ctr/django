from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["tittle", "update", "timestamp"]
    list_display_links = ["update", "timestamp"]
    search_fields = ["tittle", "content"]
    list_filter = ["timestamp"]
    list_editable =["tittle"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)