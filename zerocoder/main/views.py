from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def home(request):
    """Главная страница сайта"""
    return render(request, 'main/home.html')


def about(request):
    """Страница 'О нас'"""
    return render(request, 'main/about.html')


def services(request):
    """Страница с услугами"""
    return render(request, 'main/services.html')


@require_http_methods(["GET", "POST"])
def contact(request):
    """Страница контактов с обработкой формы"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        context = {'success_message': 'Спасибо! Ваше сообщение отправлено.'}
        return render(request, 'main/contact.html', context)

    return render(request, 'main/contact.html')
