from django.contrib import admin

# Register your models here.

from .models import Note, Category

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'reminder', 'category')
    list_editable = ('title', 'text', 'reminder','category')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_editable = ('title',)
