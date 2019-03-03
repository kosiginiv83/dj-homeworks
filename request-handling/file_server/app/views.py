import datetime
import sys, os

from django.shortcuts import render
from django.views.generic import TemplateView

from app.settings import FILES_PATH
from django.http import HttpResponse


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):

        return {
            'files': [
                {'name': 'file_name_1.txt',
                 'ctime': datetime.datetime(2018, 1, 1),
                 'mtime': datetime.datetime(2018, 1, 2)}
            ],
            'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        }


def file_content(request, file):
    with open(os.path.join(FILES_PATH, file)) as f:
        content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': file, 'file_content': content}
    )

# os.stat(os.path.join(FILES_PATH, file))
# content = open(os.path.join(FILES_PATH, file)).read()
