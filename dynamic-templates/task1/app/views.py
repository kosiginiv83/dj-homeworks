from django.shortcuts import render
from django.views.generic import TemplateView

import csv
import os.path
from app.settings import BASE_DIR


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        base = os.path.join(BASE_DIR, 'inflation_russia.csv')
        field_names = ('Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', \
                        'Aug', 'Sep', 'Oct', 'Nov', 'Des', 'Summ')
        th_names = ('Год', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', \
                    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'Всего')

        with open(base, encoding='UTF8', newline='') as file:
            file.readline()
            reader = tuple(csv.DictReader(file, fieldnames=field_names, delimiter=';'))

        context = {
            'base': reader,
            'th_names': th_names,
            'td_class': None
        }
        return render(request, self.template_name,
                      context)

#<p style="font-size: 120%; font-family: monospace; color: #cd66cc">Пример текста</p>
