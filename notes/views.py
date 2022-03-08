from django.http import Http404
from django.shortcuts import render
from .models import Note

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes-list.html', context={'notes':notes})

def note_detail(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except:
        raise Http404("Note is not found")
        

    return render(request, 'note-detail.html', context={'note':note})
    