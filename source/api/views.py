import json

from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import View


@ensure_csrf_cookie

def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class Count(View):
    def post(self, request, *args, **kwargs):
        if not request.user:
            response = JsonResponse({
                'error': 'Division by zero!'
            })
            response.status_code = 403
            return response
        data = json.loads(request.body)
        print(data)