from django.urls import path, include

from . import views

app_name = "notes"

urlpatterns = [
    # ex: http://127.0.0.1:8000/
    path("", views.notes_list, name="notes_list"),

    # path("register/", views.register, name="register"),



    path("create-note/", views.create_edit_note, name="create_note"),
    path("edit-note/<int:pk>/", views.create_edit_note, name="edit_note"),
    path("delete-note/<int:pk>/", views.delete_note, name="delete_note"),
]