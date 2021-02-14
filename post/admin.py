from django.contrib import admin
from .models import Language, Post, Statistic


admin.site.register(Language)
admin.site.register(Post)
admin.site.register(Statistic)