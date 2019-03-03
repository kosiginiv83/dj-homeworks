from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv
from app.settings import BUS_STATION_CSV


current_page = 1

with open(BUS_STATION_CSV, newline='', encoding='cp1251') as csvfile:
    reader = tuple(csv.DictReader(csvfile))[:]
'''
csvfile = open(BUS_STATION_CSV, encoding='cp1251')
reader = tuple(csv.DictReader(csvfile))
'''

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    page_param = request.GET.get('page')
    current_page = int(page_param) if page_param else 1

    len_reader = len(reader)
    (full_pages_count, last_page_count) = divmod(len_reader, 10)
    prev_page = current_page-1 if current_page>1 else 1
    next_page = current_page+1 if current_page<=full_pages_count else full_pages_count+1
    shift = 10 if current_page<=full_pages_count else last_page_count+1

    return render_to_response('index.html', context={
        'bus_stations': reader[(current_page-1) : (current_page-1) + shift],
        'current_page': current_page,
        'prev_page_url': f'bus_stations?page={prev_page}',
        'next_page_url': f'bus_stations?page={next_page}',
    })
