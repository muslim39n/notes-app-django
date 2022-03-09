from django.http import Http404
from django.shortcuts import redirect, render
from .models import Note, NoteParagraph

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes-list.html', context={'notes':notes})

def note_detail(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
        print(note)
    except:
        raise Http404("Note is not found")
        

    return render(request, 'note-detail.html', context={'note':note})
    
def new_note(request):
    if request.method == 'POST':
        note = Note.objects.create(name=request.POST['name'], color=request.POST['color'])
        note.save()
        return redirect('notes:note-detail', note_id=note.pk)


    else:
        return render(request, 'new-note.html')

def new_paragraph(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        paragraph = NoteParagraph.objects.create(note=note, body="")
        paragraph.save()

        return redirect('notes:note-detail', note_id=note.pk)

    raise Http404("Note is not found") 

def edit_paragraph(request, note_id, paragraph_id):
    if request.method == 'POST':
        paragraph = NoteParagraph.objects.get(pk=paragraph_id)
        paragraph.body = request.POST['body']
        paragraph.save()
        return redirect('notes:note-detail', note_id=note_id)

    raise Http404("Note is not found") 
    