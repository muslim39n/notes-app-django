from django.contrib import admin

from .models import Note, NoteParagraph

admin.site.register(Note)
admin.site.register(NoteParagraph)