from django.shortcuts import render
from django.views.generic import TemplateView

import os
from app.settings import STATIC_ROOT


class MainView(TemplateView):
    template_name = 'app/main.html'


class HomeView(TemplateView):
    template_name = 'app/home.html'
    def get(self, request, *args, **kwargs):
        context = {
            'img': r'C:\_my\Netology\Django\dj_hw\dynamic-templates\task2\app\static\steve.jpg',
            'path': os.path.join(STATIC_ROOT, 'steve.jpg')
        }
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'app/about.html'


class ContactsView(TemplateView):
    template_name = 'app/contacts.html'


class ExamplesView(TemplateView):
    template_name = 'app/examples.html'

    def get(self, request, *args, **kwargs):
        items = [{
            'title': 'Apple II',
            'text': 'Легенда',
            'img': 'ii.jpg'
        }, {
            'title': 'Macintosh',
            'text': 'Свежие новинки октября 1983-го',
            'img': 'mac.jpg'
        }, {
            'title': 'iMac',
            'text': 'Оригинальный и прозрачный',
            'img': 'imac.jpg'
        }]
        context = {
            'items': items
        }
        return render(request, self.template_name,
                      context)
