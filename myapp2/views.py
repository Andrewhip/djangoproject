from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ''
    return HttpResponse(f"Post from {year}<br>{text}")

class MonthPost(View):
    def get(self, request, year, month):
        text = ''
        return HttpResponse(f"Post from {month}/{year}<br>{text}")

def post_detail(request, year, month, slug):
    post = {
        'year': year,
        'title': 'Кто быстрее создаст списки в питоне, лист() или []',
        'content': 'в процессе написания очередной программы задумался над тем, какой способ создания списков будет работать быстрее',
        'slug': slug
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp2/my_template.html", context)