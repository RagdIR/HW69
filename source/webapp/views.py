from django.shortcuts import render

from webapp.models import Counts


def is_integer(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            return 'Not integer'


def index_view(request):
    data = Counts.objects.all()
    return  render(request, 'index.html', context={
        'counts': data
    })


def countAdd(request):
    if request.method == 'GET':
        answer = string_a + string_b
        return answer
