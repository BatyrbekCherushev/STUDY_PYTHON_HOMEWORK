from django.test import TestCase
from .models import Note

from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your tests here.

class NoteModelTest(TestCase):

    def setUp(self):
        self.test_note = Note.objects.create(
            title='Original Title',
            text='Original text content'
        )


        self.create_url = reverse('notes:create_note')
        self.edit_url = reverse('notes:edit_note', kwargs={'pk': self.test_note.pk})
        self.list_url = reverse("notes:index")

    def test_edit_note_view_get_404(self):
        """Перевірка, чи GET-запит на редагування неіснуючого PK повертає 404."""
        non_existing_pk = 999
        non_existent_url = reverse('notes:edit_note', kwargs={'pk': non_existing_pk})

        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, 404)

    def test_create_note_view_post_invalid_data(self):
        """Перевірка, що POST з невалідними даними повертає форму з помилками."""
        # Відправка даних, де відсутнє обов'язкове поле 'text'
        invalid_data = {
            'title': 'Short Title',
            # 'text' пропущено, і це має спричинити помилку
        }

        initial_note_count = Note.objects.count()

        response = self.client.post(self.create_url, invalid_data)

        # Перевіряємо, що ми залишилися на сторінці (статус 200)
        self.assertEqual(response.status_code, 200)
        # Перевіряємо, що нотатка НЕ була створена
        self.assertEqual(Note.objects.count(), initial_note_count)
        # Перевіряємо, що форма містить помилки
        self.assertTrue(response.context['form'].errors)

    def test_edit_note_view_post_invalid_data(self):
        """Перевірка, що при редагуванні з невалідними даними нотатка не змінюється."""
        original_title = self.test_note.title

        invalid_data = {
            'title': '',  # Припускаємо, що title не може бути порожнім
            'text': 'Some new text',
        }

        response = self.client.post(self.edit_url, invalid_data)

        # Перевіряємо, що ми залишилися на сторінці (статус 200)
        self.assertEqual(response.status_code, 200)

        # Перевіряємо, що нотатка в базі НЕ оновилася
        self.test_note.refresh_from_db()
        self.assertEqual(self.test_note.title, original_title)
        self.assertTrue(response.context['form'].errors)


    def test_delete_note_success(self):
        """Перевірка успішного видалення нотатки."""
        note_to_delete = Note.objects.create(title='To Delete', text='Delete this')
        delete_url = reverse('notes:delete_note', kwargs={'pk': note_to_delete.pk})

        initial_note_count = Note.objects.count()
        response = self.client.get(delete_url)

        # Перевірка перенаправлення
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)

        # Перевірка, що кількість нотаток зменшилася на 1
        self.assertEqual(Note.objects.count(), initial_note_count - 1)

    def test_delete_note_404(self):
        """Перевірка, що видалення неіснуючого PK повертає 404."""
        non_existing_pk = self.test_note.pk + 999
        non_existent_url = reverse('notes:delete_note', kwargs={'pk': non_existing_pk})

        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, 404)
