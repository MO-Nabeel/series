from django.contrib import admin
from .models import watched_series,watched_later_series
admin.site.register(watched_series)
admin.site.register(watched_later_series)