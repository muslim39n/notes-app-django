from django.urls import path

from .views import *

app_name = 'notes'

urlpatterns = [
    path('', notes_list, name='notes-list'),
    path('<int:note_id>/', note_detail, name='note-detail')
]