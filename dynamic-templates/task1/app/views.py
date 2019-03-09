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
            reader = list(csv.DictReader(file, fieldnames=field_names, delimiter=';'))

        base = []
        for row in reader:
            new_row = OrderedDict()
            for key, value in row.items():
                if key == 'Year': new_row[key] = {'val': value, 'class': ''}
                elif key == 'Summ': new_row[key] = {'val': value, 'class': 'grey lighten-3'}
                elif value > 5: new_row[key] = {'val': value, 'class': 'materialize-red lighten-1'}
                elif value > 2 and value <= 5: new_row[key] = {'val': value, 'class': 'materialize-red lighten-3'}
                elif value > 1 and value <= 2: new_row[key] = {'val': value, 'class': 'materialize-red lighten-5'}
                elif value < 0: new_row[key] = {'val': value, 'class': 'green lighten-3'}
                else: new_row[key] = {'val': value, 'class': ''}
            base.append(new_row)

        context = {
            'base': base,
            'th_names': th_names,

        }
        return render(request, self.template_name,
                      context)



#<p style="font-size: 120%; font-family: monospace; color: #cd66cc">Пример текста</p>
#{{ unit|add_class:"materialize-red-text text-darken-1" }}
'''
{% if unit >= 5 %}
{% endif %}

{% with "materialize-red darken-1" as td_class %}
<th class={{ td_class }}>{{ unit }}</th>
{% endwith %}
'''
