from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(News_Article)
admin.site.register(Comment)
admin.site.register(Subscription)