from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# def index(request):
#     return HttpResponse("Hello from Notes app.")

# Create your views here.
NOTES = {
    '2025-10-10': "Прийняти ліки",
    '2025-10-11': "Сходити на тренування",
    '2025-10-13':  "Проходити 10000 кроків щодня",
}
def index(request):
    template = loader.get_template("notes/index.html")
    context = {"page_name": "index",
               "notes": NOTES}
    return HttpResponse(template.render(context, request))
