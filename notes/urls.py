from django.urls import path

from .views import *

app_name = 'notes'

urlpatterns = [
    path('', notes_list, name='notes-list'),
    path('<int:note_id>/', note_detail, name='note-detail'),
    path('new/', new_note, name='new-note'),
    path('<int:note_id>/newparagraph/', new_paragraph, name='new-paragraph'),
    path('<int:note_id>/editparagraph/<int:paragraph_id>/', edit_paragraph, name='edit-paragraph'),
]