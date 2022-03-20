from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Список постов')


# В урл мы ждем параметр, и нужно его передать в функцию для использования
def group_posts_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')
