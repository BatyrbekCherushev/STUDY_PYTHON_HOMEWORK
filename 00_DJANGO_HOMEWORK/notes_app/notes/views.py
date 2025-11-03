from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Note, Category

from .forms import CreateNoteForm


# Create your views here.

def index(request):
    notes = Note.objects.all()
    template = loader.get_template("notes/index.html")

    context = {"page_name": "index",
               "page_header_title": "My notes",
               "notes": notes}
    return HttpResponse(template.render(context, request))


def create_edit_note(request, pk = None):
    if pk:
        note = get_object_or_404(Note, pk=pk)
    else:
        note = None

    if request.method == "GET":
        form = CreateNoteForm(instance=note)
    elif request.method == "POST":
        form = CreateNoteForm(request.POST, instance = note)
        if form.is_valid():
            form.save()
            return redirect("notes:index")

    context = {
        "form": form,
        "note": note,
        "page_header_title": "EDIT NOTE" if note else "CREATE NOTE"
    }

    return render(request, "notes/create_note.html", context)

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("notes:index")