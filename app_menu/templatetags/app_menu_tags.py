from django import template
from django.template.loader import render_to_string
from app_menu.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # Получаем URL текущей страницы
    current_path = context['request'].path.strip('/')

    # Получаем все пункты меню
    menu_items = Menu.objects.filter(title=menu_name).order_by('pk').prefetch_related('children')

    # Генерируем и Возвращаем HTML-код меню с помощью шаблонаHTML-код в виде HttpResponse
    return render_to_string('menu.html', {'menu_items': menu_items, 'current_path': current_path})