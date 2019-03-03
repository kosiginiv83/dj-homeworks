from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    fromLanding = request.GET.get('from-landing')
    counter_click[fromLanding] += 1

    return render_to_response('index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')
    counter_show[ab_test_arg] += 1
    page = 'landing.html' if ab_test_arg == 'original' else 'landing_alternate.html'
    
    return render_to_response(page)


def stats(request):
    test_conversion = 'none'
    original_conversion = 'none'

    if counter_show['test']:
        test_conversion = counter_click['test'] / counter_show['test']
        test_conversion = round(test_conversion, 2)
    if counter_show['original']:
        original_conversion = counter_click['original'] / counter_show['original']
        original_conversion = round(original_conversion, 2)

    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
