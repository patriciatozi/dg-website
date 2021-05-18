from django.contrib import admin
from .models import Post, Tag, SocialMedia

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(SocialMedia)
