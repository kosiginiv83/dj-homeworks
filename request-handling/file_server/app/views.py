from datetime import datetime, date
import sys, os

from django.shortcuts import render
from django.views.generic import TemplateView

from app.settings import FILES_PATH
from django.http import HttpResponse


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, year=1970, month=1, day=1):
        files = []
        for file in os.listdir(FILES_PATH):
            stats = os.stat(os.path.join(FILES_PATH, file))
            ctime = datetime.fromtimestamp(stats.st_ctime).timetuple()
            mtime = datetime.fromtimestamp(stats.st_mtime).timetuple()
            files.append({
                'name': file,
                'ctime': datetime(ctime[0], ctime[1], ctime[2]),
                'mtime': datetime(mtime[0], mtime[1], mtime[2])
            })


        return {
            'file': files,
            #'date': None
            #'date': date(year, month, day)
        }
        '''
        return {
            'files': [
                {'name': 'file_name_1.txt',
                 'ctime': datetime.datetime(2018, 1, 1),
                 'mtime': datetime.datetime(2018, 1, 2)}
            ],
            'date': datetime.date(2018, 1, 1)  # Этот параметр необязательный
        }
        '''


def file_content(request, file):
    with open(os.path.join(FILES_PATH, file)) as f:
        content = f.read()

    files = []
    for file in os.listdir(FILES_PATH):
        stats = os.stat(os.path.join(FILES_PATH, file))
        ctime = datetime.fromtimestamp(stats.st_ctime).timetuple()
        mtime = datetime.fromtimestamp(stats.st_mtime).timetuple()
        files.append({
            'name': file,
            'ctime': datetime(ctime[0], ctime[1], ctime[2], ctime[3], ctime[4]),
            'mtime': datetime(mtime[0], mtime[1], mtime[2], mtime[3], mtime[4])
        })

    return render(
        request,
        'file_content.html',
        context={'file_name': file, 'file_content': files}
    )

# context={'file_name': file, 'file_content': content}
# os.stat(os.path.join(FILES_PATH, file))
# content = open(os.path.join(FILES_PATH, file)).read()
