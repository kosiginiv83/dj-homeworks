from django.shortcuts import render
from django.views.generic import TemplateView

import csv
from app.settings import BASE_DIR


class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        base = os.path.join(BASE_DIR, 'inflation_russia.csv')
        with open(base) as csv:
            reader = tuple(csv.DictReader(csv))[:]

        context = {
            'base': reader
        }
        return render(request, self.template_name,
                      context)
