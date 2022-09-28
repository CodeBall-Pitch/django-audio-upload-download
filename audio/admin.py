from django.contrib import admin
from .models import Song
# Register your models here.
admin.site.site_header="Audio Panel"
admin.site.site_title="Admin Panel"

admin.site.register(Song)