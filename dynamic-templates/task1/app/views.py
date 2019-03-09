from django.shortcuts import render
from django.views.generic import TemplateView

import csv
import os.path
from app.settings import BASE_DIR
from collections import OrderedDict


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

        reader = [ {key: (float(value.strip()) if (key != 'Year' and value != '') else \
                    value) for key, value in x.items()} for x in reader ]

        base = []
        for row in reader:
            new_row = OrderedDict()
            for key, value in row.items():
                if value == '': new_row[key] = {'val': '-', 'class': ''}
                elif key == 'Year': new_row[key] = {'val': value, 'class': ''}
                elif key == 'Summ': new_row[key] = {'val': value, 'class': 'grey lighten-3'}
                elif value > 5: new_row[key] = {'val': value, 'class': 'red darken-3'}
                elif value > 2 and value <= 5: new_row[key] = {'val': value, 'class': 'red'}
                elif value > 1 and value <= 2: new_row[key] = {'val': value, 'class': 'red lighten-3'}
                elif value < 0: new_row[key] = {'val': value, 'class': 'green lighten-3'}
                else: new_row[key] = {'val': value, 'class': ''}
            base.append(new_row)

        context = {
            'base': base,
            'th_names': th_names,

        }
        return render(request, self.template_name,
                      context)
