from django.contrib import admin
from .models import Post
# Get the Blog table we created to the ADMIN SITE
admin.site.register(Post)
